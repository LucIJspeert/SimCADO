import pytest

from simcado import UserCommands
from simcado.optics import imager2 as imager

from synphot import SpectralElement

# things that the imager needs to dc
# exist with nothing
# accept a UserCommands object
# have an attribute which pulls in all mirrors
# hold a list of transmission curves, emission curves
# create a list of fields of view
#
# make an OpticalTrain
# make a combined


@pytest.fixture(scope="class")
def opt_empty():
    cmd = UserCommands()
    cmd.validate()
    opt = imager.Imager(cmd)
    return opt

@pytest.fixture(scope="class")
def opt_scao_wide():
    cmd = UserCommands(sim_data_dir="mocks/MICADO_SCAO_WIDE/",
                       filename="mocks/MICADO_SCAO_WIDE/"
                                "mock_MICADO_SCAO_WIDE.config")
    cmd.validate()
    opt = imager.Imager(cmd)
    return opt


@pytest.mark.usefixtures("opt_scao_wide")
class TestImagerInit:
    def test_initialises_with_nothing(self):
        opt = imager.Imager()
        assert type(opt) == imager.Imager

    def test_accepts_usercommands(self, opt_scao_wide):
        assert opt_scao_wide.cmds["INST_FILTER_TC"] == "Ks"


@pytest.mark.usefixtures("opt_scao_wide", "opt_empty")
class TestImagerSurfacesAttr:
    def test_returns_empty_table_when_opt_is_empty(self, opt_empty):
        assert len(opt_empty.surfaces) == 0

    def test_returns_full_table_for_existing_table_files(self, opt_scao_wide):
        assert len(opt_scao_wide.surfaces) == 19


class TestMakeSurfacesTable:

    def test_returns_empty_table_for_no_filenames(self):
        surf_tbl = imager.make_surfaces_table()
        assert len(surf_tbl) == 0

    def test_returns_single_table_when_only_one_filename_is_passed(self):
        files = ["mocks/MICADO_SCAO_WIDE/EC_mirrors_ELT.tbl"]
        surf_tbl = imager.make_surfaces_table(files)
        assert len(surf_tbl) == 5
        assert "Mirror" in surf_tbl.colnames

    def test_returns_combined_table(self):
        files = ["mocks/MICADO_SCAO_WIDE/EC_mirrors_ELT.tbl",
                 "mocks/MICADO_SCAO_WIDE/EC_mirrors_SCAO_relay.tbl",
                 "mocks/MICADO_SCAO_WIDE/EC_mirrors_MICADO_Wide.tbl"]
        surf_tbl = imager.make_surfaces_table(files)
        assert len(surf_tbl) == 19
        assert "Mirror" in surf_tbl.colnames

    def test_returns_none_for_bogus_table(self):
        surf_tbl = imager.make_surfaces_table(["bogus.tbl"])
        assert len(surf_tbl) == 0

    def test_ignores_tables_which_dont_exist_but_doesnt_throw_error(self):
        files = ["mocks/MICADO_SCAO_WIDE/EC_mirrors_ELT.tbl",
                 "bogus.tbl"]
        surf_tbl = imager.make_surfaces_table(files)
        assert len(surf_tbl) == 5
        assert "Mirror" in surf_tbl.colnames


@pytest.mark.usefixtures("opt_scao_wide")
class TestMakeSpectralCurveFromFile:
    def test_throw_exception_when_file_doesnt_exist(self, opt_scao_wide):
        with pytest.raises(ValueError):
            imager.make_spectral_curve_from_file("bogus.dat")

    def test_reads_ok_for_existing_file(self):
        file = "mocks/MICADO_SCAO_WIDE/TC_filter_Ks.dat"
        curve = imager.make_spectral_curve_from_file(file)
        assert type(curve) == SpectralElement

    def test_reads_reflectivity_if_exists(self):
        file = "mocks/MICADO_SCAO_WIDE/TER_dichroic.dat"
        curve = imager.make_spectral_curve_from_file(file,
                                                     val_name="reflectivity")
        assert type(curve) == SpectralElement

    def test_raises_error_if_colname_doesnt_exist(self):
        pass





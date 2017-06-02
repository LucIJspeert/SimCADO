"""Unit tests for module simcado.source"""
import pytest
import numpy as np
import simcado as sim

def test_rotate():
    """Test method Source.rotate

    Points are rotated by 90 degrees.
    """

    x_in = np.array([1., 0., 1.])
    y_in = np.array([0., 1., 1.])
    x_out = np.array([0., -1., -1.])
    y_out = np.array([1., 0., 1.])

    src = sim.source.stars(x=x_in, y=y_in)
    src.rotate(angle=90., unit="degree")
    assert np.allclose(src.x, x_out)
    assert np.allclose(src.y, y_out)

    src.rotate(angle=90., unit="degree", use_orig_xy=True)
    assert np.allclose(src.x, x_out)
    assert np.allclose(src.y, y_out)


def test_shift():
    """Test method Source.shift"""
    d_x, d_y = 1.5, -0.3

    x_in = np.array([1., 0., 1.])
    y_in = np.array([0, 1., 1.])
    x_out = np.array([2.5, 1.5, 2.5])
    y_out = np.array([-0.3, 0.7, 0.7])

    src = sim.source.stars(x=x_in, y=y_in)
    src.shift(dx=d_x, dy=d_y, use_orig_xy=False)
    assert np.allclose(src.x, x_out)
    assert np.allclose(src.y, y_out)

    src.shift(dx=d_x, dy=d_y, use_orig_xy=True)
    assert np.allclose(src.x, x_out)
    assert np.allclose(src.y, y_out)


def test_spectrum_sum_over_range():
    """Test function spectrum_sum_over_range"""
    lam = np.array([1.0, 1.1, 1.2])
    flux = np.array([[1., 1., 1.]])

    flux_1 = sim.source.spectrum_sum_over_range(lam, flux, 0.95, 1.25)
    assert np.allclose(flux_1, 3.)

    flux_2 = sim.source.spectrum_sum_over_range(lam, flux, 1., 1.2)
    assert np.allclose(flux_2, 2.)

    flux_3 = sim.source.spectrum_sum_over_range(lam, flux, 1.05, 1.15)
    assert np.allclose(flux_3, 1.)

    with pytest.raises(ValueError):
        flux_4 = sim.source.spectrum_sum_over_range(lam, flux, 1.15, 1.05)



def test_stars_params():
    # Test combinations of input parameters
    assert sim.source.stars()
    assert sim.source.stars("G2V", 15)
    assert sim.source.stars("G2V", [15, 12])
    assert sim.source.stars(['G2V', 'F2V'], 15)
    assert sim.source.stars(["G2V", "F2V"], [15, 12])


def test_source_resample_equivalency():

    n=8

    im = np.ones((100,100))
    lam, spec = sim.source.SED("M0V", "K", 20)
    src = sim.source.source_from_image(im, lam, spec, 0.004, oversample=n)
    hdu, (cmd, opt, fpa) = sim.run(src, return_internals=True)

    im = np.ones((n*100, n*100)) / (n**2)
    lam, spec = sim.source.SED("M0V", "K", 20)
    src2 = sim.source.source_from_image(im, lam, spec, 0.004/n, oversample=1)
    hdu2, (cmd2, opt2, fpa2) = sim.run(src2, return_internals=True)

    diff = np.sum(np.abs(fpa2.chips[0].array) - np.abs(fpa.chips[0].array)) / \
                                                    np.sum(fpa.chips[0].array)

    assert diff < 1E-4


def test_stars_delivers_the_same_as_SED():

    #sim.source.stars([])

    spec_types = ["A0V", "A0V", "M5V"]
    lam, spec = sim.source.SED(spec_type=spec_types[0],
                               filter_name="Ks",
                               magnitude=20.)
    vega_SED  = sim.spectral.EmissionCurve(lam=lam, val=spec)
    vega_star = sim.source.stars(spec_types=spec_types[0],
                                 filter_name="Ks",
                                 mags=20)

    assert np.sum(vega_SED.val) == np.sum(vega_star.spectra[0] * \
                                                            vega_star.weight[0])

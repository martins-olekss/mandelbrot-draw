<?php
// Source: https://stackoverflow.com/questions/3725522/fractals-explained

/// Construct a complex number from two reals
function cpl($re, $im) {
    return array($re, $im);
}


/// Add two complex numbers.
function cadd($p, $q) {
    return cpl(
        $p[0] + $q[0],
        $p[1] + $q[1]);
}

/// Multiply two complex numbers.
function cmul($p, $q) {
    return cpl(
        $p[0] * $q[0] - $p[1] * $q[1],
        $p[0] * $q[1] + $p[1] * $q[0]);
}

/// Return the norm of the complex number.
function cmod($p) {
    return sqrt($p[0] * $p[0] + $p[1] * $p[1]);
}


function is_in_mandelbrot_set($c, $iterations)
{
    $z = cpl(0, 0);
    do {
        if (cmod($z) >= 2)
            return false;
        $z = cadd(cmul($z, $z), $c);
    } while ($iterations--);
    return true;
}


function mandelbrot($img, $w, $h)
{
    $color = imagecolorallocate($img, 0xFF, 0, 0);
    $zoom = 400;
    $iters = 30;
    for ($x = 0; $x < $w; $x++) {
        for ($y = 0; $y < $h; $y++) {
            // scale our integer points
            // to be small real numbers around 0
            $px = ($x - $w / 2) / $zoom;
            $py = ($y - $h / 2) / $zoom;
            $c = cpl($px, $py);
            if (is_in_mandelbrot_set($c, $iters)) {
                imagesetpixel($img, $x, $y, $color);
            }
        }
    }

    return $img;
}

$w = 600;
$h = 600;

header("Content-type: image/png");
imagepng(mandelbrot(imagecreatetruecolor($w, $h), $w, $h));
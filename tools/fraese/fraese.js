"use strict";
var Material;
(function (Material) {
    Material[Material["GussAluminium"] = 0] = "GussAluminium";
    Material[Material["AluminiumKnetlegierung"] = 1] = "AluminiumKnetlegierung";
    Material[Material["Weichkunststoff"] = 2] = "Weichkunststoff";
    Material[Material["Hartkunststoff"] = 3] = "Hartkunststoff";
    Material[Material["HolzHart"] = 4] = "HolzHart";
    Material[Material["HolzWeich"] = 5] = "HolzWeich";
    Material[Material["MDF"] = 6] = "MDF";
    Material[Material["Messing"] = 7] = "Messing";
    Material[Material["Kupfer"] = 8] = "Kupfer";
    Material[Material["Stahl"] = 9] = "Stahl";
})(Material || (Material = {}));
const vc = new Map([
    [Material.GussAluminium, 500],
    [Material.AluminiumKnetlegierung, 500],
    [Material.Weichkunststoff, 600],
    [Material.Hartkunststoff, 550],
    [Material.HolzHart, 450],
    [Material.HolzWeich, 500],
    [Material.MDF, 450],
    [Material.Messing, 365],
    [Material.Kupfer, 365],
    [Material.Stahl, 90]
]);
const zahnvorschub = new Map([
    [Material.GussAluminium, [0.01, 0.01, 0.01, 0.015, 0.015, 0.025, 0.0275, 0.03, 0.034, 0.038, 0.044, 0.05]],
    [Material.AluminiumKnetlegierung, [0.01, 0.02, 0.025, 0.05, 0.05, 0.05, 0.057, 0.064, 0.074, 0.08, 0.09, 0.1]],
    [Material.Weichkunststoff, [0.025, 0.03, 0.035, 0.045, 0.065, 0.09, 0.095, 0.1, 0.15, 0.2, 0.25, 0.3]],
    [Material.Hartkunststoff, [0.015, 0.02, 0.025, 0.05, 0.06, 0.08, 0.0845, 0.089, 0.0945, 0.1, 0.125, 0.15]],
    [Material.HolzHart, [0.02, 0.025, 0.03, 0.035, 0.045, 0.055, 0.0555, 0.056, 0.068, 0.08, 0.085, 0.09]],
    [Material.HolzWeich, [0.025, 0.03, 0.035, 0.04, 0.05, 0.06, 0.065, 0.07, 0.0775, 0.085, 0.0925, 0.1]],
    [Material.MDF, [0.03, 0.04, 0.045, 0.05, 0.06, 0.07, 0.075, 0.08, 0.085, 0.09, 0.0955, 0.11]],
    [Material.Messing, [0.015, 0.02, 0.025, 0.025, 0.03, 0.05, 0.053, 0.056, 0.0605, 0.065, 0.0725, 0.08]],
    [Material.Stahl, [0.01, 0.01, 0.012, 0.025, 0.03, 0.038, 0.0415, 0.045, 0.0475, 0.05, 0.065, 0.08]]
]);
function drehzahl(material, durchmesser) {
    let fz;
    let zv = zahnvorschub.get(material);
    if (durchmesser < 1 || durchmesser > zv.length) {
        throw new Error("Durchmesser nicht im zulässigen Bereich");
    }
    if (Math.floor(durchmesser) === durchmesser) {
        fz = zv[durchmesser - 1];
    }
    else {
        let fz1 = zv[Math.floor(durchmesser) - 1];
        let fz2 = zv[Math.ceil(durchmesser) - 1];
        fz = fz1 + (fz2 - fz1) * (durchmesser - Math.floor(durchmesser));
    }
    return fz * 1000 / durchmesser;
}

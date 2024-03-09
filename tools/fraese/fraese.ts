enum Material {
  "GussAluminium",
  "AluminiumKnetlegierung",
  "Weichkunststoff",
  "Hartkunststoff",
  "HolzHart",
  "HolzWeich",
  "MDF",
  "Messing",
  "Stahl"
}

const vcData: Map<Material, number> =
  new Map([
    [Material.GussAluminium, 500],
    [Material.AluminiumKnetlegierung, 500],
    [Material.Weichkunststoff, 600],
    [Material.Hartkunststoff, 550],
    [Material.HolzHart, 450],
    [Material.HolzWeich, 500],
    [Material.MDF, 450],
    [Material.Messing, 365],
    [Material.Stahl, 90]
  ]);

const zahnvorschub: Map < Material, Array<number>> =
  new Map([
    [Material.GussAluminium,          [0.01, 0.01, 0.01,  0.015, 0.015, 0.025, 0.0275, 0.03,  0.034, 0.038, 0.044, 0.05]],
    [Material.AluminiumKnetlegierung, [0.01, 0.02, 0.025, 0.05,  0.05,  0.05,  0.057,  0.064, 0.074, 0.08,  0.09,  0.1]],
    [Material.Weichkunststoff,        [0.025, 0.03, 0.035, 0.045,0.065, 0.09,  0.095,  0.1,   0.15,  0.2,   0.25,  0.3]],
    [Material.Hartkunststoff,         [0.015, 0.02, 0.025, 0.05, 0.06,  0.08,  0.0845, 0.089, 0.0945,0.1,   0.125, 0.15]],
    [Material.HolzHart,               [0.02, 0.025, 0.03, 0.035, 0.045, 0.055, 0.0555, 0.056, 0.068, 0.08,  0.085, 0.09]],
    [Material.HolzWeich,              [0.025, 0.03, 0.035, 0.04, 0.05,  0.06,  0.065,  0.07,  0.0775,0.085, 0.0925,0.1]],
    [Material.MDF,                    [0.03, 0.04, 0.045, 0.05,  0.06,  0.07,  0.075,  0.08,  0.085, 0.09,  0.0955,0.11]],
    [Material.Messing,                [0.015, 0.02, 0.025, 0.025, 0.03, 0.05,  0.053,  0.056, 0.0605,0.065, 0.0725,0.08]],
    [Material.Stahl,                  [0.01, 0.01, 0.012, 0.025, 0.03,  0.038, 0.0415, 0.045, 0.0475,0.05,  0.065, 0.08]]
]);

function drehzahl(material: Material, durchmesser: number): number {

  let vc = vcData.get(material)!;
  return (vc * 1000) / (3.14 * durchmesser);
}

function vorschub(material: Material, durchmesser: number): number {

  let zaehne = 2;
  let vf: number; // Vorschubgeschwindigkeit
  let fz: number; // Zahnvorschub
  let fz_mat = zahnvorschub.get(material)!;

  if (durchmesser < 1 || durchmesser > fz_mat.length) {
    throw new Error("Durchmesser nicht im zulässigen Bereich");
  }

  if (Math.floor(durchmesser) === durchmesser) {
    fz = fz_mat[durchmesser - 1];
  } else {
    let fz_floor = fz_mat[Math.floor(durchmesser) - 1];
    let fz_ceil = fz_mat[Math.ceil(durchmesser) - 1];
    fz = fz_floor + (fz_ceil - fz_floor) * (durchmesser - Math.floor(durchmesser));
  }
  vf = fz * drehzahl(material, durchmesser) * zaehne;

  return vf;
}

function updatePage(event) {

  event.preventDefault();
  let material = document.getElementById("material").value;
  let durchmesser = document.getElementById("durchmesser").value;
  let upm = drehzahl(Material[material], durchmesser);
  let mmpm = vorschub(Material[material], durchmesser);

  document.getElementById("drehzahl").innerHTML = upm.toFixed(2);
  document.getElementById("vorschub").innerHTML = mmpm.toFixed(2);
}
let divInputRecherche = document.getElementById("divInputRecherche");
let divInputWrench = document.getElementById("divWrench");
let divInputContrat = document.getElementById("divContrat");
let divInputPlus = document.getElementById("divPlus");

let inputRecherche  = document.getElementById("inputRecherche");
let linkWrench  = document.getElementById("linkWrench");
let linkContrat  = document.getElementById("linkContrat");
let linkPlus  = document.getElementById("linkPlus");

divInputRecherche.addEventListener(
    'click', 
    () => { inputRecherche.focus(); }
);
divInputWrench.addEventListener(
    'click', 
    () => { linkWrench.click(); }
);
divInputContrat.addEventListener(
    'click', 
    () => { linkContrat.click(); }
);     
divInputPlus.addEventListener(
    'click', 
    () => { linkPlus.click(); }
);     
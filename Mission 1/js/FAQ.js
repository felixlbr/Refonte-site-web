/*
	Liste des rubriques de la barre de navigation
*/
const listeRubriques = document.getElementsByClassName('listeRubriques');

/*
	Liste des contenus de toutes les rubriques
*/
const contenuRubriques = 	document.getElementsByClassName("rubrique");

/*
	Liste de toutes les questions
*/
const questions = 	document.getElementsByClassName("question");

/*
	Fonction qui ajoute une "class" à un élément "elt"
*/
function addClass(elt, className){
	elt.classList.add(className);
}

/*
	Fonction qui retire une "class" à un élément
*/
function removeClass(elt, className){
	elt.classList.remove(className);
}

/*
	Fonction qui remplace la class "oldClass" par la class "newClass" pour un élément elt
*/
function switchClass(elt, newClass, oldClass){
	removeClass(elt, oldClass);
	addClass(elt, newClass);
}
/*
	Affiche la réponse sélectionnée et cache les autres
*/
function afficher_reponse(qr, q){
	let questionsReponses = qr.getElementsByClassName('question-reponse');
	
	for (const questionReponse of questionsReponses){		
		let question =  questionReponse.getElementsByClassName('question')[0];
		let reponse  =  questionReponse.getElementsByClassName('reponse')[0];

		if (question.getAttribute('id') === q.getAttribute('id')){
			reponse.style.display ="block";
			question.setAttribute("data-icone", "-");
		} else {
			reponse.style.display ="none";
			question.setAttribute("data-icone", "+");
		}
	}
}

/*
	Affiche les questions/réponses de la rubrique sélectionnée et cache les autres
*/
function afficher_rubrique(r){
	for (const rubrique of listeRubriques){
		// On affiche les questions de la rubrique cliquée
		for(const contenuRubrique of contenuRubriques){
			if(contenuRubrique.getAttribute('rub') === r.getAttribute('rub')){
				contenuRubrique.style.display = "block";
			} else {
				contenuRubrique.style.display = "none";
			}
		}
		
		// On marque la rubrique cliquée
		if(rubrique.getAttribute('id') === r.getAttribute('id')){
			switchClass(rubrique, "selected", "notSelected");
		} else {
			switchClass(rubrique, "notSelected", "selected");
		}
	}
}

/*
	Pour chaque rubrique de la variable "listeRubriques", on va ajouter
	dynamiquement un listener d'évenements en demandant
	d'éxécuter la fonction cliqueRubrique à chaque fois que
	l'utilisateur clique sur une de ces listeRubriques
*/
for (const rubrique of listeRubriques){
	rubrique.addEventListener('click', function cliqueSurRubrique(event) {
		afficher_rubrique(rubrique);
	}); 
}

/*
	Pour chaque question de la variable "questions", on va ajouter
	dynamiquement un listener d'évènement en demandant
	d'éxécuter la fonction cliqueSurQuestion à chaque fois que
	l'utilisateur clique sur une de ces questions
*/
for (const question of questions){
	question.addEventListener('click', function cliqueSurQuestion(event) {
		for(const contenuRubrique of contenuRubriques){
			const questionsReponses = contenuRubrique.getElementsByClassName('question-reponse');
			
			for(const questionReponse of questionsReponses){
				if(question.getAttribute('id') === questionReponse.getElementsByClassName('question')[0].getAttribute('id')){
					afficher_reponse(contenuRubrique, question);
					break;
				}
			}
		}
	});
}

var sidenav = document.getElementById("mySidenav");
var openBtn = document.getElementById("openBtn");
var closeBtn = document.getElementById("closeBtn");

openBtn.onclick = openNav;
closeBtn.onclick = closeNav;

/* Set the width of the side navigation to 250px */
function openNav() {
  sidenav.classList.add("active");
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  sidenav.classList.remove("active");
}
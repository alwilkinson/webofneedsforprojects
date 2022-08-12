"use strict";

const projectsList = document.getElementById("projectList");
const searchBar = document.getElementById("searchBar");
let projects = [];

searchBar.addEventListener("keyup", (e) => {
  //   console.log(e.target.value);
  const searchString = e.target.value.toLowerCase();

  const filteredProjects = projects.filter((project) => {
    return (
      project.name.toLowerCase().includes(searchString) ||
      project.tags.toLowerCase().includes(searchString)
    );
  });
  displayProjects(filteredProjects);
});

/*
Feature needs fixing  
Needs to find way to connect to fast api and pull from projects endpoint
*/
const loadProjects = async () => {
  try {
    // var Airtable = require("airtable");
    // var base = new Airtable({ apiKey: "key7NVws8AO4SCLvl" }).base(
    //   "appAyRuk6f9ewiH78"
    // );
    // const table = base("Projects");
    const res = await fetch("https://hp-api.herokuapp.com/api/characters");
    projects = await res.json();
    displayProjects(projects);
  } catch (err) {
    console.error(err);
  }
};

/* 
Feature needs fixing
Will get projects from FASTAPI and display them
*/
const displayProjects = (projects) => {
  const htmlString = projects
    .map((project) => {
      return `
      <li class="project">
      <h2>Heavenya</h2>
      <p>Tags: NodeJS, React, React Native</p>
      <img src="images/Heavenya-400x210 (1).png"></img>
  </li>

  <li class="project">
  <h2>Oreino</h2>
  <p>Tags: HTML CSS Christianity</p>
  <img src="images/Heavenya-400x210 (1).png"></img>
</li>
        `;
    })
    .join("");
  //projectsList.innerHTML = htmlString;
};

loadProjects();

//Code will allow user to click project to learn more
const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnOpenModal = document.querySelectorAll(".project");

//when any button is clicked modal and overlay will appear by removing hidden class
const openModal = function () {
  modal.classList.remove("hidden"); //no dot needed when removing class
  overlay.classList.remove("hidden");
};

//upon function call both pop up window and blur overlay are hidden
const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

//Waits for button to be clicked to run function
for (let i = 0; i < btnOpenModal.length; i++) {
  btnOpenModal[i].addEventListener("click", openModal);
}

btnCloseModal.addEventListener("click", closeModal); //when X is clicked window closes
overlay.addEventListener("click", closeModal); //when blurred background clicked window closes

/*
-addEventListener waits for certain event
-'keydown' waits for key press
-'keyup' waits for key release
-'keypressed' waits for a key to be held
- e variable for event and can be used cause we define function within event listener and its not called
*/
document.addEventListener("keydown", function (e) {
  //if key pressed is esc and modal does not contain class hidden function runs
  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});

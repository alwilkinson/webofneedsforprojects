"use strict";

const projectsList = document.getElementById("projectList");
const searchBar = document.getElementById("searchBar");
let projects = [];
var Airtable = require("airtable");
var base = new Airtable({ apiKey: "key7NVws8AO4SCLvl" }).base(
  "appAyRuk6f9ewiH78"
);

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

const loadProjects = async () => {
  try {
    // var Airtable = require("airtable");
    // var base = new Airtable({ apiKey: "key7NVws8AO4SCLvl" }).base(
    //   "appAyRuk6f9ewiH78"
    // );
    const table = base("Projects");
    //const res = await fetch("https://hp-api.herokuapp.com/api/characters");
    projects = await table.select().firstPage();
    displayProjects(projects);
  } catch (err) {
    console.error(err);
  }
};

const displayProjects = (projects) => {
  const htmlString = projects
    .map((project) => {
      return `
            <li class="project">
                <h2>${project.name}</h2>
                <p>Tags: ${project.tags}</p>
                <img src="${project.image}"></img>
            </li>
        `;
    })
    .join("");
  projectsList.innerHTML = htmlString;
};

loadProjects();

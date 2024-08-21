/* Created by Tivotal */

let btn = document.querySelector(".toogler");
let btnIcon = document.querySelector("#icon");
let content = document.querySelector(".content");

btn.onclick = function () {
  if (content.getAttribute("data-theme") != "dark") {
    content.setAttribute("data-theme", "dark");
    btnIcon.setAttribute("class", "fas fa-solid fa-sun");
  } else {
    content.setAttribute("data-theme", "");
    btnIcon.setAttribute("class", "fas fa-solid fa-moon");
  }
};

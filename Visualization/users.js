(function() {
  index = 1;
  infohtml = "";
  var container = document.getElementById("usersContainer");
  var currentRow = document.createElement("div");
  currentRow.className = "row";
  for (var user in users) {
    var newUser = document.createElement("div");
    newUser.className = "col-md-3 col-xs-3 users";
    newUser.innerHTML = users[user].name;
    newUser.setAttribute("place", index-1);
    newUser.onclick = fn;
    newUser.onmouseover = mousein;
    newUser.onmouseout = mouseout;
    currentRow.appendChild(newUser);
    if (index % 4 === 0 || index === users.length) {
      container.appendChild(currentRow);
      var newRow = document.createElement("div");
      newRow.className = "row";
      currentRow = newRow;
    }
    index++;
  }
})();

function mousein() {
  infohtml = document.getElementById("info").innerHTML;
  var place = Number(this.getAttribute("place"));
  user = users[place];
  infoDisplay(user);
}

function mouseout() {
  document.getElementById("info").innerHTML = infohtml;
}

function fn() {
  var place = Number(this.getAttribute("place"));
  user = users[place];
  infoDisplay(user, true);
}

function infoDisplay(user, manual=false) {
  var info = document.getElementById("info");
  var inside = "<h2>" + user.name + "</h2>"
  if (user.coaches.length > 0) {
    inside += "<p>Coaches: " + user.coaches.join(", ") + "</p>";
  } else {
    inside += "<p>No Coaches</p>"
  }
  if (user.trainees.length > 0) {
    inside += "<p>Trainees: " + user.trainees.join(", ") + "</p>";
  } else {
    inside += "<p>No Trainees</p>"
  }
  inside += "<p>Version: " + user.version + "</p>";
  info.innerHTML = inside;
  if (manual === true) { infohtml = inside; }
}

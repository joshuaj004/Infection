(function() {
  index = 1;
  infohtml = "";
  versions = new Set();
  onVersions = []
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
    newUser.setAttribute("version", users[user].version);
    versions.add(users[user].version);
    currentRow.appendChild(newUser);
    if (index % 4 === 0 || index === users.length) {
      container.appendChild(currentRow);
      var newRow = document.createElement("div");
      newRow.className = "row";
      currentRow = newRow;
    }
    index++;
  }
  var versions = [...versions];
  versions.sort();
  var checkboxes = document.getElementById("checkboxes");
  for (var v in versions) {
    var newLabel = document.createElement("label");
    var newCheckbox = document.createElement("input");
    var newBreak = document.createElement("br");
    newCheckbox.type = "checkbox";
    newLabel.value = versions[v];
    newLabel.onclick = function() {
      boxClicked(this.value);
    };
    newLabel.appendChild(newCheckbox);
    newLabel.innerHTML += versions[v];
    checkboxes.appendChild(newLabel);
    checkboxes.appendChild(newBreak);
  }
})();

function boxClicked(value) {
  if (onVersions.includes(value)) {
    onVersions.splice(onVersions.indexOf(value), 1);
  } else {
    onVersions.push(value)
  }
  versionUsers = document.querySelectorAll("div.users");
  for (var i = 0; i < versionUsers.length; i++) {
    var tempUser = versionUsers[i];
    var number = Number(versionUsers[i].getAttribute("version"));
    if (onVersions.includes(number) === true) {
      if (!versionUsers[i].className.includes(" selected")) {
        versionUsers[i].className += " selected";
      }
    } else if (onVersions.includes(number) === false) {
      versionUsers[i].className = versionUsers[i].className.replace(" selected", "");
    } else {
      // do nothing
    }
  }
}

function mousein() {
  infohtml = document.getElementById("info").innerHTML;
  var place = Number(this.getAttribute("place"));
  var user = users[place];
  infoDisplay(user);
}

function mouseout() {
  document.getElementById("info").innerHTML = infohtml;
}

function fn() {
  var place = Number(this.getAttribute("place"));
  var user = users[place];
  infoDisplay(user, true);
}

function infoDisplay(user, manual=false) {
  var info = document.getElementById("info");
  var inside = "<h2>" + user.name + "</h2>"
  if (user.coaches.length > 0) {
    inside += "<p>Coach: " + user.coaches.join(", ") + "</p>";
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

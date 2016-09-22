(function() {
  // onload function
  index = 1;
  infohtml = "";
  // Creates a set to store the various versions of all of the Users
  versions = new Set();
  // An array with the versions whose checkboxes are checked
  onVersions = []
  var container = document.getElementById("usersContainer");
  var currentRow = document.createElement("div");
  currentRow.className = "row";
  for (var user in users) {
    var newUser = document.createElement("div");
    // Sets up the bootstrap classes
    newUser.className = "col-md-3 col-xs-3 users";
    newUser.innerHTML = users[user].name;
    newUser.setAttribute("place", index-1);
    // Handles the user clicking on a User
    newUser.onclick = fn;
    // Handles the user hovering over a User
    newUser.onmouseover = mousein;
    newUser.onmouseout = mouseout;
    newUser.setAttribute("version", users[user].version);
    versions.add(users[user].version);
    currentRow.appendChild(newUser);
    // Sets the default information
    if (index === 1) {
      infoDisplay(users[0], true);
    }
    // Creates a new row every 4 Users or at the end of the User list
    if (index % 4 === 0 || index === users.length) {
      container.appendChild(currentRow);
      var newRow = document.createElement("div");
      newRow.className = "row";
      currentRow = newRow;
    }
    index++;
  }
  // Unpacks the versions Set into a versions Array so that it can be sorted
  var versions = [...versions];
  versions.sort();
  var checkboxes = document.getElementById("checkboxes");
  // Creates the checkboxes with the versions that Users have
  for (var v in versions) {
    var newLabel = document.createElement("label");
    var newCheckbox = document.createElement("input");
    var newBreak = document.createElement("br");
    var checkValue = document.createElement("p");
    checkValue.innerHTML = versions[v];
    checkValue.style.margin = "0px";
    newCheckbox.type = "checkbox";
    newCheckbox.value = Number(versions[v]);
    newCheckbox.onclick = function() {
      boxClicked(this.value);
    };
    newLabel.appendChild(newCheckbox);
    newLabel.appendChild(checkValue);
    checkboxes.appendChild(newLabel);
    checkboxes.appendChild(newBreak);
  }
})();

function boxClicked(value) {
  value = Number(value);
  // Checks for the current checkbox value in the list of turned on Versions
  // Used for toggling the classes
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
  // Helper function for infoDisplay
  var place = Number(this.getAttribute("place"));
  var user = users[place];
  infoDisplay(user, true);
}

function infoDisplay(user, manual=false) {
  // Handles the user clicking on a User or mousing over a User
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

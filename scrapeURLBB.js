a = document.getElementById("listContainer_databody");
b = a.querySelectorAll("a");

myarray = [];

for (let i = 0; i < b.length; i += 3) {
  nametext = b[i].textContent;
  cleantext = nametext.replace(/\s+/g, " ").trim();
  cleanlink = b[i].href;
  myarray.push([cleantext, cleanlink]);
}

function make_table() {
  let table = "<table><thead><th>Name</th><th>Links</th></thead><tbody>";
  for (let i = 0; i < myarray.length; i++) {
    table +=
      "<tr><td>" + myarray[i][0] + "</td><td>" + myarray[i][1] + "</td></tr>";
  }

  let w = window.open("");
  w.document.write(table);
}

make_table();

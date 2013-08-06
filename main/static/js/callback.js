function callback_horario(data){
	console.log(data.materias[1]);
	var wrap = $(".wrap");
	var sectionM = document.createElement("section");
	for (var i = 0; i < data.materias.length; i++) {
		var mat = document.createElement("div");
		mat.innerHTML = data.materias[i];
		sectionM.appendChild(mat);
	};
	wrap.append(sectionM);
	cambios();
	alert("listo!!!");
}

function callback_inscripcion(data){
	console.log(data.row);
    cambios();
    var row = data.row;
    if (row == null) {
    	alert("Ingrese la url, por favor!!!");
    };
    var master_table = document.getElementById("table");
    for (var i = 0; i < row.length; i++) {
    	var article = document.createElement("article");
    	article.setAttribute("class", "row");
    	var cell = row[i];
    	for (var j = 0; j < cell.length; j++) {
    		var div = document.createElement("div");
    		if (i == 0) {
    			div.setAttribute("class", "dia");
    		} else {
    			if (cell[j] != "&nbsp;") {
	    			div.setAttribute("class", "hora");
	    		};
    		};
    		div.innerHTML = cell[j];
    		article.appendChild(div);
    	};
    	master_table.appendChild(article);
    };
}

function resCombi(data) {
    alert("numero de combinaciones de materias: " + data);
}
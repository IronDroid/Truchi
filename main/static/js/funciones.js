$(document).on("ready",inicio);
function inicio () {
	$("#input_button").on("click", esconder);
	$(".innerbar li").on("click", mostrar);
	$(".tile").on("click",detalle);
}

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

function detalle(data){
	console.log(data);
	var offset = {
		width: 103,
		left: data.currentTarget.offsetLeft,
		top: data.currentTarget.offsetTop+70
	}
	$("#detalle").css(offset);
	var detalle = document.getElementById("detalle");
	detalle.innerHTML = data.currentTarget.id;
}

function esconder(){
	var cambio = {
		height: "45px",
		overflow: "hidden"
	}
	$("#url_form").css(cambio);
	var subtitle = document.getElementById("subtitle_form");
	subtitle.innerHTML = "Espere por favor ;)";
}

function mostrar(data){
	$(".info").removeClass("active");
	$(".apuntes").removeClass("active");
	$(".record").removeClass("active");
	$(".config").removeClass("active");
	$("."+data.currentTarget.id).addClass("active");
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
function cambios(){
	var cambioCSS = {
		height: "700px"
	}
	$("#contain-table").css(cambioCSS);
	var cambioUrl = {
		height: "0px",
		overflow: "hidden",
		margin: "0px",
		padding: "0px"
	}
	$("#url_form").css(cambioUrl);
	var cambioIns = {
		height: "0px",
		overflow: "hidden",
		margin: "0px",
		padding: "0px"
	}
	$("#instruccion").css(cambioIns);
}
$(document).on("ready",inicio);
function inicio () {
	$("#input_button").on("click", esconder);
	$(".innerbar li").on("click", mostrar);
	$(".tile").on("click",detalle);
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
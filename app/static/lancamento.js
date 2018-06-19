var stop;
var dataInicio;
var horaInicio;
var dataFim;
var horaFim;
function iniciar(){
    var data = new Date();
    var dia     = ("0" + data.getDate()).slice(-2);           // dia com 2 digitos.
    var mes     = ("0" + (data.getMonth() + 1)).slice(-2)     // mês com 2 digitos
    var ano4    = data.getFullYear();       // 4 dígitos
    var hora    = data.getHours();          // 0-23
    var min     = data.getMinutes();        // 0-59
    dataInicio = ano4 + '-' + mes + '-' + dia;
    horaInicio = hora + ':' + min;
    $("#dataInicio").val(dataInicio);
    $("#horaInicio").val(horaInicio);
    //alert(descricao);
    // Mostra o resultado
    //alert('Hoje é ' + dataInicial + ' às ' + horaInicial);
    seg = 0;
    min = 0;
    hora = 0;
    $("#iniciar").css("display", "none");
    $("#parar").css("display", "inline-block");
    stop = setInterval(function(){
        $("#time").html(hora+":"+min+":"+seg);
        seg++;
        if(seg == 60){
            min++;
            seg = 0;
        }
        if(min == 60){
            hora++;
            min=0;
        }
    }, 1000);
}
function parar(){
    clearInterval(stop);
    var data = new Date();
    var dia     = ("0" + data.getDate()).slice(-2);           // 1-31
    var mes     = ("0" + (data.getMonth() + 1)).slice(-2)          // 0-11 (zero=janeiro)
    var ano4    = data.getFullYear();       // 4 dígitos
    var hora    = data.getHours();          // 0-23
    var min     = data.getMinutes();        // 0-59
        // Formata a data e a hora (note o mês + 1)
    dataFim = ano4 + '-' + mes + '-' + dia;
    horaFim = hora + ':' + min;
    $("#dataFim").val(dataFim);
    $("#horaFim").val(horaFim);
    $("#parar").css("display", "none");

}

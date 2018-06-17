var start = false;
var stop;
var dataInicial;
var horaInicial;
function iniciar(){
    if(start){
        return(0);
    }else{
        start = true;
    }
    var data = new Date();
    var dia     = data.getDate();           // 1-31
    var mes     = data.getMonth();          // 0-11 (zero=janeiro)
    var ano4    = data.getFullYear();       // 4 dígitos
    var hora    = data.getHours();          // 0-23
    var min     = data.getMinutes();        // 0-59
        // Formata a data e a hora (note o mês + 1)
    dataInicial = dia + '/' + (mes+1) + '/' + ano4;
    horaInicial = hora + ':' + min;

    // Mostra o resultado
    //alert('Hoje é ' + dataInicial + ' às ' + horaInicial);
    seg = 0;
    min = 0;
    hora = 0;
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
    if(!start){
        return(0);
    }else{
        start = false;
    }
    clearInterval(stop);
    $("#time").html("");
}
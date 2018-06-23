$('#pesquisar').keyup(function(){
    var $this = $(this);
    var pesquisa = $this.val();
    console.log(pesquisa);
    var achouAlgo = false;
    console.log(pesquisa.length);
    for(var j = 0; j < lancamentos.length; j++){
        if(pesquisa == lancamentos[j].id){
            achouAlgo = true;
            $("#listaLancamentos").html(
                "<tbody>"+
                    "<tr>"+
                        "<td><h3>Código</h3></td>"+
                        "<td><h3>Data Inicio</h3></td>"+
                        "<td><h3>Hora Inicio</h3></td>"+
                        "<td><h3>Data Fim</h3></td>"+
                        "<td><h3>Hora Fim</h3></td>"+
                        "<td><h3>Total Horas</h3></td>"+
                        "<th></th>"+
                    "</tr>"+
                    "<tr>"+
                        "<td>"+lancamentos[j].id+"</td>"+
                        "<td>"+lancamentos[j].dataInicio+"</td>"+
                        "<td>"+lancamentos[j].horaInicio+"</td>"+
                        "<td>"+lancamentos[j].dataFim+"</td>"+
                        "<td>"+lancamentos[j].horaFim+"</td>"+
                        "<td>"+lancamentos[j].horasTrabalhadas+"</td>"+
                        "<td>"+
                        "<a href='/admin/vinculacao/editar/"+lancamentos[j].id+"'>"+
                        "<button class='btn btn-primary'>"+
                        "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                        "</a>"+
                        "<a href='/admin/lancamento/detalhes/"+lancamentos[j].id+"'>"+
                        "<button class='btn btn-info'>"+
                        "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                        "</a>"+
                        "<a href='/admin/lancamento/deletar/"+lancamentos[j].id+"'>"+
                        "<button class='btn btn-danger'>"+
                        "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                        "</a>"+
                        "</td>"+
                    "</tr>"+
                "</tbody>"
            );
        }
    }

    if(pesquisa.length == 0){
        var lista = "";
        for(var j = 0; j < lancamentos.length; j++){
            console.log('append');
            achouAlgo = true;
            lista = lista +
            "<tr>"+
                "<td>"+lancamentos[j].id+"</td>"+
                "<td>"+lancamentos[j].dataInicio+"</td>"+
                "<td>"+lancamentos[j].horaInicio+"</td>"+
                "<td>"+lancamentos[j].dataFim+"</td>"+
                "<td>"+lancamentos[j].horaFim+"</td>"+
                "<td>"+lancamentos[j].horasTrabalhadas+"</td>"+
                "<td>"+
                "<a href='/admin/lancamento/editar/"+lancamentos[j].id+"'>"+
                "<button class='btn btn-primary'>"+
                "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                "</a>"+
                "<a href='/admin/lancamento/detalhes/"+lancamentos[j].id+"'>"+
                "<button class='btn btn-info'>"+
                "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                "</a>"+
                "<a href='/admin/lancamento/deletar/"+lancamentos[j].id+"'>"+
                "<button class='btn btn-danger'>"+
                "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                "</a>"+
                "</td>"+
            "</tr>";
        }
        console.log(lista);
        $("#listaLancamentos").html(
        "<tbody>"+
            "<tr>"+
                "<td><h3>Código</h3></td>"+
                "<td><h3>Data Inicio</h3></td>"+
                "<td><h3>Hora Inicio</h3></td>"+
                "<td><h3>Data Fim</h3></td>"+
                "<td><h3>Hora Fim</h3></td>"+
                "<td><h3>Total Horas</h3></td>"+
                "<th></th>"+
            "</tr>"+
        lista+"</tbody>");
    }

    if(!achouAlgo){
        console.log(achouAlgo);
        $("#listaLancamentos").html("<tbody></tbody>");
    }
});
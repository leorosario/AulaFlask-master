$('#pesquisar').keyup(function(){
    var $this = $(this);
    var pesquisa = $this.val();
    console.log(pesquisa);
    var achouAlgo = false;
    console.log(pesquisa.length);
    for(var j = 0; j < atividades.length; j++){
        if(pesquisa == atividades[j].id){
            achouAlgo = true;
            $("#listaAtividades").html(
                "<tbody>"+
                    "<tr>"+
                        "<td><h3>Cod Atividade</h3></td>"+
                        "<td><h3>Descrição</h3></td>"+
                        "<th></th>"+
                    "</tr>"+
                    "<tr>"+
                        "<td>"+atividades[j].id+"</td>"+
                        "<td>"+atividades[j].descricao+"</td>"+
                        "<td>"+
                        "<a href='/admin/atividades/editar/"+atividades[j].id+"'>"+
                        "<button class='btn btn-primary'>"+
                        "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                        "</a>"+
                        "<a href='/admin/atividades/detalhes/"+atividades[j].id+"'>"+
                        "<button class='btn btn-info'>"+
                        "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                        "</a>"+
                        "<a href='/admin/atividades/deletar/"+atividades[j].id+"'>"+
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
        for(var j = 0; j < atividades.length; j++){
            console.log('append');
            achouAlgo = true;
            lista = lista +
            "<tr>"+
                "<td>"+atividades[j].id+"</td>"+
                "<td>"+atividades[j].descricao+"</td>"+
                "<td>"+
                "<a href='/admin/atividades/editar/"+atividades[j].id+"'>"+
                "<button class='btn btn-primary'>"+
                "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                "</a>"+
                "<a href='/admin/atividades/detalhes/"+atividades[j].id+"'>"+
                "<button class='btn btn-info'>"+
                "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                "</a>"+
                "<a href='/admin/atividades/deletar/"+atividades[j].id+"'>"+
                "<button class='btn btn-danger'>"+
                "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                "</a>"+
                "</td>"+
            "</tr>";
        }
        console.log(lista);
        $("#listaAtividades").html(
        "<tbody>"+
            "<tr>"+
                "<td><h3>Cod Atividade</h3></td>"+
                "<td><h3>Descrição</h3></td>"+
                "<th></th>"+
            "</tr>"+
        lista+"</tbody>");
    }

    if(!achouAlgo){
        console.log(achouAlgo);
        $("#listaAtividades").html("<tbody></tbody>");
    }
});
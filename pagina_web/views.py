from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import qrcode


def index(request):
    return render(request, "pagina_web/index.html")


def qrcode_view(request):
    return render(request, 'pagina_web/qrcode.html')


def chamada(request):
    return render(request, 'pagina_web/chamada.html')


def configuracao(request):
    return render(request, 'pagina_web/configuracao.html')

    #imagem_qrcode = qrcode.make(link)
    # Para mudar a extensão do arquivo penas mude o final .png para a extensão desejável
    #
    #gerar_qrcode("https://www.udf.edu.br")
def gerar_qrcode(request):
    if request.method == 'POST':
        turma = request.POST.get('turma')  # Obtém a turma enviada no formulário
        if turma:
            imagem_qrcode = qrcode.make(f"link/{turma}")  # Gera o QR Code com a turma selecionada
            response = HttpResponse(content_type="image/png")  # Define o tipo de conteúdo como imagem PNG

            # Salva a imagem diretamente na resposta HTTP
            imagem_qrcode.save(response, "PNG")

            return response
        else:
            # Caso não tenha selecionado uma turma
            return HttpResponse("Erro: Nenhuma turma selecionada", status=400)

    return render(request, 'pagina_web/qrcode.html')
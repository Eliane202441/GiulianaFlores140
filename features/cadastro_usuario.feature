Feature: Cadastro de usuario

Scenario: Cadastro de usuario 
Given que estou no site https://www.giulianaflores.com.br/
When clico no link Perfil 
And clico no campo login/Cadastro
And clico no campo criar Cadastro
And preencho o campo Nome Completo com Jennifer Ana Clara Freitas
And preencho o campo CPF com 161.727.368-68
And preencho o campo E-mail com jenneifer_anafreitas@toysbrasil.com.br
And preencho o campo Senha com @123Sucesso
And preencho o campo CEP com 06240-010 e ok
And preencho o campo numero com 20
And preencho o campo telefone com 11999780280
Then preencho o campo Finalizar 


Scenario: login positivo
Given que estou no site https://www.giulianaflores.com.br/
When clico no link Perfil 
And clico no campo login/Cadastro
And preencho o campo com o CPF 776.631.466-54
And clico no campo Senha !Saopaulo123
Then clico no campo continuar


Scenario: login negativo
Given que estou no site https://www.giulianaflores.com.br/
When clico no link Perfil 
And clico no campo login/Cadastro
And preencho o campo com o CPF 776.631.466-54
And clico no campo Senha !Saopaulo456
And clico no campo continuar
Then exibe a mensagem Atenção email ou senha invalido!

Scenario: Selecionar produto
Given que estou no site https://www.giulianaflores.com.br/
When clico no link Perfil 
And clico no campo login/Cadastro
And preencho o campo com o CPF 776.631.466-54
And clico no campo Senha !Saopaulo123
And clico no campo continuar
And clico no menu presentes
And clico no campo CEP com 06240-110
And seleciono o campo endereço
And clico no campo aplicar
And clico em Buque 50 rosas vermelhas
Then clicar  no campo adicionar ao carrinho


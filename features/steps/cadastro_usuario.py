
from pyexpat.errors import messages
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que estou no site https://www.giulianaflores.com.br/')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(40)
    context.driver.get("https://www.giulianaflores.com.br/")

@when(u'clico no link {perfil}')
def step_impl(context, perfil):         
    context.driver.find_element(By.ID, "perfil-hidden").click()
@when(u'clico no campo login/Cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "UrlLogin").click()  

@when(u'clico no campo criar Cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click() 
    time.sleep(5) 

@when(u'preencho o campo Nome Completo com Jennifer Ana Clara Freitas')
def step_impl(context):
 context.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Jennifer Ana Clara Freitas")

 @when(u'preencho o campo CPF com 161.727.368-68')
 def step_impl(context):  
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("161.727.368-68")

 @when(u'preencho o campo E-mail com jenneifer_anafreitas@toysbrasil.com.br')
 def step_impl(context):
    context.driver.find_element(By.ID,"ContentSite_txtEmail").send_keys("jenneifer_anafreitas@toysbrasil.com.br")
 
@when(u'preencho o campo Senha com @123Sucesso')
def step_impl(context):
    context.driver.find_element(By.NAME, "ctl00$ContentSite$txtPasswordNew").send_keys("@123Sucesso")

@when(u'preencho o campo CEP com 06240-010 e ok')
def step_impl(context):
    context.driver.find_element(By.ID,"ContentSite_CustomerAddress_txtZip").send_keys("06240-010")
 
@when(u'preencho o campo numero com 20')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys(20)

@when(u'preencho o campo telefone com 11999780280')
def step_impl(context):
 context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11999780280")


@then(u'preencho o campo Finalizar')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()

#@then(u'exibir a mensagem cadastro realizado com sucesso')
#def step_impl(context):   
   # success_message = context.driver.find_element(By.XPATH, f"//div[contains(text(), '{"cadastro realizado comsucesso"}')]")
    #assert success_message.is_displayed()
    #context.driver.quit()

    # login positivo

@when(u'clico no campo login/Cadastrar')
def step_impl(context):
    context.driver.find_element(By.ID, "UrlLogin").click()


@when(u'preencho o campo com o CPF 776.631.466-54')
def step_impl(context):
  context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("776.631.466-54")  

@when(u'clico no campo Senha !Saopaulo123')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("!Saopaulo123")

@then(u'clico no campo continuar')
def step_impl(context):
   context.driver.find_element(By.ID, "ContentSite_ibtContinue").click() 



### login negativo

@when(u'clico no campo Senha !Saopaulo456')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("!Saopaulo456")


@when(u'clico no campo continuar')
def step_impl(context):
   context.driver.find_element(By.ID, "ContentSite_ibtContinue").click() 
 

@then(u'exibe a mensagem Atenção email ou senha invalido!')
def step_impl(context):
 mensagem = context.driver.find_element(By.CSS_SELECTOR, ".font_erro").text
 print("Mensagem recebida:", messages)


## selecionar produto


@when(u'clico no menu presentes')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".link-menu-desktop").click()

@when(u'clico no campo CEP com 06240-110')
def step_impl(context):
    context.driver.find_element(By.ID, "inputSearchAddress").send_keys("06240-110")

@when(u'seleciono o campo endereço')
def step_impl(context):
    elemento_endereco = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".itemAddress.selectedItemAddress"))
    )

@when(u'clico no campo aplicar')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".apply-button").click()

@when(u'clico em Buque 50 rosas vermelhas')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".title-item").click()


@then(u'clicar  no campo adicionar ao carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()





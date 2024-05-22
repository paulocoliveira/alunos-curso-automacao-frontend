package com.example; // Define o pacote para a classe

import org.junit.jupiter.api.BeforeEach; // Importa a anotação @BeforeEach do JUnit 5
import org.junit.jupiter.api.Test; // Importa a anotação @Test do JUnit 5
import org.junit.jupiter.api.AfterEach; // Importa a anotação @AfterEach do JUnit 5
import org.openqa.selenium.By; // Importa a classe By do Selenium para localizar elementos
import org.openqa.selenium.WebDriver; // Importa a interface WebDriver do Selenium
import org.openqa.selenium.chrome.ChromeDriver; // Importa a classe ChromeDriver do Selenium
import org.openqa.selenium.chrome.ChromeOptions; // Importa a classe ChromeOptions para configurar opções do Chrome
import java.time.Duration; // Importa a classe Duration para definir a duração do tempo de espera implicitamente
import java.time.LocalDateTime; // Importa a classe LocalDateTime para trabalhar com data e hora
import java.time.format.DateTimeFormatter; // Importa a classe DateTimeFormatter para formatar data e hora
import java.util.concurrent.TimeUnit; // Importa a classe TimeUnit para configurar tempos de espera

public class DateTimeTest { // Define a classe de testes
    private WebDriver driver; // Declara uma variável para a instância do WebDriver

    @BeforeEach // Anotação que indica que este método deve ser executado antes de cada teste
    public void setUp() {
        ChromeOptions options = new ChromeOptions(); // Cria uma instância de ChromeOptions
        options.addArguments("--remote-allow-origins=*"); // Adiciona um argumento para permitir origens remotas
        driver = new ChromeDriver(options); // Inicializa o ChromeDriver com as opções configuradas
        driver.manage().window().maximize(); // Maximiza a janela do navegador
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10)); // Define um tempo de espera implícito de 10 segundos para encontrar elementos
        driver.get("https://paulocoliveira.github.io/mypages/plugins/index.html"); // Navega até a URL especificada
    }

    @Test // Anotação que indica que este método é um teste
    public void testDateTimeManipulation() {
        driver.findElement(By.xpath("//button[text()='DateTime']")).click(); // Encontra e clica no botão "DateTime" usando XPath
        LocalDateTime currentDateTime = LocalDateTime.now(); // Obtém a data e hora atual
        driver.findElement(By.id("current_time")).sendKeys(currentDateTime.toString()); // Insere a data e hora atual no campo com ID "current_time"
        DateTimeFormatter formatter1 = DateTimeFormatter.ofPattern("dd-MM-yy"); // Formata a data para o formato dia-mês-ano
        DateTimeFormatter formatter2 = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"); // Formata a data e hora para o formato ano-mês-dia hora:minuto:segundo
        driver.findElement(By.id("formatted_date1")).sendKeys(currentDateTime.format(formatter1)); // Insere a data formatada no campo com ID "formatted_date1"
        driver.findElement(By.id("formatted_date2")).sendKeys(currentDateTime.format(formatter2)); // Insere a data e hora formatadas no campo com ID "formatted_date2"
        driver.findElement(By.id("date_in_60_days")).sendKeys(currentDateTime.plusDays(60).format(formatter1)); // Calcula a data 60 dias à frente e insere no campo com ID "date_in_60_days"
        driver.findElement(By.id("year_2099")).sendKeys(currentDateTime.withYear(2099).format(DateTimeFormatter.ofPattern("dd-MM-yyyy"))); // Ajusta o ano para 2099 e insere no campo com ID "year_2099"
        driver.findElement(By.xpath("//button[text()='CONCLUIR']")).click(); // Encontra e clica no botão "CONCLUIR" usando XPath
        try {
            Thread.sleep(5000); // Aguarda 5 segundos para observar o resultado da operação
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // Trata a interrupção do Thread.sleep()
        }
    }

    @AfterEach // Anotação que indica que este método deve ser executado após cada teste
    public void tearDown() {
        driver.quit(); // Fecha o navegador
    }
}

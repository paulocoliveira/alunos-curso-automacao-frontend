using NUnit.Framework; // Importa o namespace do NUnit, que é o framework de testes que estamos usando.
using OpenQA.Selenium; // Importa o namespace do Selenium WebDriver.
using OpenQA.Selenium.Chrome; // Importa o namespace específico para o ChromeDriver.
using System; // Importa o namespace do System, que inclui classes essenciais como DateTime.
using System.Threading; // Importa o namespace para funcionalidades de threading, como Thread.Sleep.

namespace SeleniumTests { // Define o namespace do projeto, organizando as classes sob este nome.
    public class DateTimeManipulationTests { // Define a classe de testes.
        private IWebDriver driver; // Declara uma variável para a instância do WebDriver.

        [SetUp] // Atributo do NUnit que indica que este método deve ser executado antes de cada teste.
        public void SetUp() {
            driver = new ChromeDriver(); // Inicializa o ChromeDriver.
            driver.Manage().Window.Maximize(); // Maximiza a janela do navegador.
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10); // Define um tempo de espera implícito de 10 segundos para encontrar elementos.
            driver.Navigate().GoToUrl("https://paulocoliveira.github.io/mypages/plugins/index.html"); // Navega até a URL especificada.
        }

        [Test] // Atributo do NUnit que indica que este método é um teste.
        public void TestDateTimeManipulation() {
            driver.FindElement(By.XPath("//button[text()='DateTime']")).Click(); // Encontra e clica no botão "DateTime" usando XPath.
            DateTime currentDateTime = DateTime.Now; // Obtém a data e hora atual.
            driver.FindElement(By.Id("current_time")).SendKeys(currentDateTime.ToString("yyyy-MM-dd HH:mm:ss")); // Insere a data e hora atual formatada no campo com ID "current_time".
            driver.FindElement(By.Id("formatted_date1")).SendKeys(currentDateTime.ToString("dd-MM-yy")); // Insere a data formatada no campo com ID "formatted_date1".
            driver.FindElement(By.Id("formatted_date2")).SendKeys(currentDateTime.ToString("yyyy-MM-dd HH:mm:ss")); // Insere a data e hora formatadas no campo com ID "formatted_date2".
            driver.FindElement(By.Id("date_in_60_days")).SendKeys(currentDateTime.AddDays(60).ToString("dd-MM-yy")); // Calcula a data 60 dias à frente e insere no campo com ID "date_in_60_days".
            driver.FindElement(By.Id("year_2099")).SendKeys(currentDateTime.AddYears(2099 - currentDateTime.Year).ToString("dd-MM-yyyy")); // Ajusta o ano para 2099 e insere no campo com ID "year_2099".
            driver.FindElement(By.XPath("//button[text()='CONCLUIR']")).Click(); // Encontra e clica no botão "CONCLUIR" usando XPath.
            Thread.Sleep(5000); // Aguarda 5 segundos para observar o resultado da operação.
        }

        [TearDown] // Atributo do NUnit que indica que este método deve ser executado após cada teste.
        public void TearDown() {
            if (driver != null) { // Verifica se o driver não é nulo.
                driver.Quit(); // Fecha o navegador.
                driver.Dispose(); // Libera os recursos do WebDriver.
            }
        }
    }
}

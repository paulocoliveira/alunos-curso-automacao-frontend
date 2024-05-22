const { Builder, By, Key, until } = require('selenium-webdriver');
require('chromedriver');

describe('DateTime manipulation tests', function () {
    let driver;

    before(async function () {
        driver = await new Builder().forBrowser('chrome').build(); // Constrói uma nova instância do navegador Chrome
        await driver.manage().window().maximize(); // Maximiza a janela do navegador
        await driver.get('https://paulocoliveira.github.io/mypages/plugins/index.html'); // Acessa a URL desejada
    });

    it('testDateTimeManipulation', async function () {
        await driver.findElement(By.xpath("//button[text()='DateTime']")).click(); // Clica no botão "DateTime"
        const currentDateTime = new Date(); // Obtém a data e hora atual
        await driver.findElement(By.id("current_time")).sendKeys(currentDateTime.toISOString()); // Insere a data e hora atual no formato ISO
        const formatted1 = currentDateTime.toLocaleDateString('en-GB').split('/').reverse().join('-'); // Formata a data para o formato dia-mês-ano
        await driver.findElement(By.id("formatted_date1")).sendKeys(formatted1); // Insere a data formatada no campo
        const formatted2 = currentDateTime.toISOString().replace('T', ' ').substring(0, 19); // Formata a data e hora para o formato ano-mês-dia hora:minuto:segundo
        await driver.findElement(By.id("formatted_date2")).sendKeys(formatted2); // Insere a data e hora formatadas no campo
        const dateIn60Days = new Date(currentDateTime.getTime() + (60 * 24 * 60 * 60 * 1000)); // Calcula a data 60 dias à frente
        await driver.findElement(By.id("date_in_60_days")).sendKeys(dateIn60Days.toLocaleDateString('en-GB').split('/').reverse().join('-')); // Insere a data 60 dias à frente formatada no campo
        const in2099 = new Date(currentDateTime.setFullYear(2099)); // Ajusta o ano para 2099
        await driver.findElement(By.id("year_2099")).sendKeys(in2099.toLocaleDateString('en-GB').split('/').reverse().join('-')); // Insere a data com ano ajustado para 2099 no campo
        await driver.findElement(By.xpath("//button[text()='CONCLUIR']")).click(); // Clica no botão "CONCLUIR"
        await driver.sleep(5000); // Aguarda 5 segundos
    });

    after(() => driver && driver.quit()); // Fecha o navegador e encerra a sessão do WebDriver
});

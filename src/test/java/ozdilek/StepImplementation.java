package ozdilek;
import com.thoughtworks.gauge.Step;
import io.appium.java_client.MobileElement;
import org.openqa.selenium.By;

public class StepImplementation extends BaseTest {
    public StepImplementation() {
    }

    @Step({"<time> saniye bekle"})
    public void waitTime(int time) throws InterruptedException {
        Thread.sleep(1000 * time);
    }

    @Step({"<Keys> Id'li elemente tıkla"})
    public void clickElementByid(String Key) {
        appiumDriver.findElement(By.id(Key)).click();
        System.out.println(Key + "Elementine tıklandı");
    }

    @Step({"<Key> Id'li elemente <keyword> değerini yaz"})
    public void SendkeyElementByid(String Key, String keyword) {
        appiumDriver.findElement(By.id(Key)).sendKeys(keyword);
        System.out.println(Key + "Elementine tıklandı");
    }

    @Step({"<Keys> xpath'li elemente tıkla"})
    public void clickElementByxpath(String Key) {
        appiumDriver.findElement(By.xpath(Key)).click();
        System.out.println(Key + "Elementine tıklandı");
    }


    @Step({"<Key> xpath'li elemente <keyword> değerini yaz"})
    public void SendkeyElementByxpath(String Key, String keyword) {
        appiumDriver.findElement(By.xpath(Key)).sendKeys(keyword);
        System.out.println(Key + "Elementine tıklandı");
    }


}

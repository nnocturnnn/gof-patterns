
import java.util.List;

public class Man implements Observer {
    String name;

    public Man(String name) {
        this.name = name;
    }
    
    @Override
    public void handleEvent(List<String> mails) {
        System.out.println("Dear " + name + "we have letter for you:" + mails);
    }
}
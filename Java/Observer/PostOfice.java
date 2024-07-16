
import java.util.ArrayList;
import java.util.List;

public class PostOfice implements Observed {
    List<String> mails = new ArrayList<>();
    List<Observer> subscribers = new ArrayList<>();

    public void addMail (String mail) {
        this.mails.add(mail);
        notifyObserver();
    }

    public void removeMail(String mail) {
        this.mails.remove(mail);
        notifyObserver();
    }

    @Override
    public void addObserver(Observer observer) {
        this.subscribers.add(observer);

    }
    @Override
    public void removeObserver(Observer observer) {
        this.subscribers.remove(observer);
    }
    @Override
    public void notifyObserver() {
        for (Observer observer : subscribers)
            observer.handleEvent(this.mails);
    }
}
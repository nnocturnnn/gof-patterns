

public class ObserverMail {
    public static void main(String[] args) {
        PostOfice postOfice = new PostOfice();

        postOfice.addMail("firs letter");
        postOfice.addMail("second letter");

        Observer firsMan = new Man("Andrey Ge");

        postOfice.addObserver(firsMan);
        postOfice.addMail("third mail");
        postOfice.removeMail("firs letter");
    }
}
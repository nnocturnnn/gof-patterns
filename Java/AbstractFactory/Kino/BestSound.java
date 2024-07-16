package AbstractFactory.Kino;
import AbstractFactory.Music;

public class BestSound implements Music {
    public String[] language = "English";
    @Override
    public void playMusic() {
        System.out.println("Best Music Play on " + language + " language");
    } 
}
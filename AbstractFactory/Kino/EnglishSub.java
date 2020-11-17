package AbstractFactory.Kino;
import AbstractFactory.Sub;

public class EnglishSub implements Sub {
    public String[] language = BestSound.language;
    @Override
    public void playSub() {
        System.out.println(language + "subtitres play");
    }
}
package AbstractFactory.Kino;
import AbstractFactory.*;

public class Film implements FilmProject {
    @Override
    public Music getMusic() {
        return new BestSound();
    }
    @Override
    public Sub getSub() {
        return new EnglishSub();
    }
    @Override
    public Video getVideo() {
        return new FullHd();
    }
}
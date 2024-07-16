package AbstractFactory;
import AbstractFactory.Kino.Film;

public class FilmRentFactory {
    public static void main(String[] args) {
        FilmProject nFilm = new Film();
        Music music = nFilm.getMusic();
        Video video = nFilm.getVideo();
        Sub sub = nFilm.getSub();
    }
}
package AbstractFactory.Kino;
import AbstractFactory.Video;
import jdk.javadoc.internal.doclets.formats.html.SourceToHTMLConverter;

public class FullHd implements Video {
    @Override
    public void playVideo() {
        System.out.println("FullHd video play");
    }
}
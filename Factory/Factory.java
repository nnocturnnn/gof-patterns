
import java.util.Random;

class Factory {
    public Figure create(int typeFigure) {
        switch (random_number1) {
            case 0: return new Triangel();
            case 1: return new Rectangel();
        }
    }
}
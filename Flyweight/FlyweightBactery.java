

import java.util.ArrayList;
import java.util.List;

public class FlyweightBactery {
    public static void main(String[] args) {
        BacteryFactory bacteryFactory = new BacteryFactory();

        List<Bactery> bacterys = new ArrayList<>();
        bacterys.add(bacteryFactory.getBacteryBySpeciality("Mito"));
        bacterys.add(bacteryFactory.getBacteryBySpeciality("Mito"));
        bacterys.add(bacteryFactory.getBacteryBySpeciality("EAO"));
        bacterys.add(bacteryFactory.getBacteryBySpeciality("Mito"));
        bacterys.add(bacteryFactory.getBacteryBySpeciality("EAO"));

        for (Bactery bactery: bacterys);
            bactery.beBactery();
    }
}
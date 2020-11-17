

import java.util.HashMap;
import java.util.Map;

public class BacteryFactory {
    private static final Map<String, Bactery> bacterys = new HashMap<>();

    public Bactery getBacteryBySpeciality(String speciality) {
        Bactery bactery = bacterys.get(speciality);

        if (bactery == null) {
            switch (speciality) {
                case "EAO":
                    System.out.println("Get EAO Bactery");
                    bactery = new EAO();
                    break;
                case "Mito":
                    System.out.println("Get Mito Bactery");
                    bactery = new Mito();
                    break;
            }
            bacterys.put(speciality, bactery);

        }
        return bactery;
    }
}
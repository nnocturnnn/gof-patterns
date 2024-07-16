

public class StrategyGame {
    public static void main(String[] args) {
        Elf elf = new Elf();
        Troll troll = new Troll();
        Vampire vampire = new Vampire();

        elf.setActivity(new GoAndFly());
        elf.executeActivity();

        troll.setActivity(new Go());
        troll.executeActivity();

        vampire.setActivity(new Fly());
        vampire.executeActivity();
    }
}
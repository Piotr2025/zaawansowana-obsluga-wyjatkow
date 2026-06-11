// Symulacja wyjątków biznesowych 
class DatabaseException extends Exception { public DatabaseException(String m, Throwable c) { super(m, c); } }
class UserNotFoundException extends RuntimeException { public UserNotFoundException(String m, Throwable c) { super(m, c); } }

public class Main {
    public static void main(String[] args) {
        try {
            // Niska warstwa rzuciła błąd bazy danych:
            throw new DatabaseException("FATAL: password authentication failed", null);
        } 
        // TODO: Złap DatabaseException a następnie zrób wyjątek UserNotFoundException,
        //       przekazując oryginalny wyjątek jako drugi argument, aby zachować oryginalny Stack Trace.
        catch (DatabaseException e) {
        }
    }
}

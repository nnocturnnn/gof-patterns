### Creational Patterns
1. **Singleton** - allows you to create only one instance of an object.  
   *Example: only one Database connection.*
2. **Factory Method** - allows creating different instances of objects using a dictionary, avoiding IF statements.  
   *Example: GET, POST, PUT, DELETE handlers.*
3. **Abstract Factory** - allows creating a factory of factories.  
   *Example: Factory of Factories.*
4. **Prototype** - creates new objects by copying an existing object (deep copy).  
   *Example: base Docker container.*
5. **Builder** - allows creating complex objects part by part.  
   *Example: building an SQL query (Base, Filters, Limits, Sorts).*

### Structural Patterns
1. **Adapter** - allows incompatible interfaces to work together.  
   *Example: connecting Internal and External APIs.*
2. **Bridge** - helps connect one interface to another.  
   *Example: connecting SQL and NoSQL databases through a bridge.*
3. **Facade** - provides a simplified interface to a complex system.  
   *Example: Interface to all Microservices.*
4. **Composite** - helps to work with objects and nested objects of the same type.  
   *Example: Module manager with a hierarchical structure.*
5. **Decorator** - extends the functionality of an object.  
   *Example: Python decorator.*
6. **Flyweight** - helps use less memory and time by sharing as much data as possible.  
   *Example: caching strategy in backend systems.*
7. **Proxy** - adds a level of abstraction before accessing an object.  
   *Example: like VPN or Authorization.*

### Behavioural Patterns
1. **Memento** - Captures and restores an object's internal state.  
   *Example: GIT snapshot of a repository.*
2. **Command** - Encapsulates a request as an object.  
   *Example: Git revert.*
3. **Interpreter** - Defines a grammatical representation for a language and an interpreter to interpret the grammar.  
   *Example: SQL or regular expression parsing.*
4. **Chain of Responsibility** - Passes a request along a chain of handlers.  
   *Example: Backend API request processing pipeline.*
5. **Iterator** - Provides a way to access elements of a collection.  
   *Example: Iterating over a collection.*
6. **Mediator** - Defines an object that encapsulates how a set of objects interact.  
   *Example: Middleware.*
7. **Observer** - Notifies dependents when an object changes state.  
   *Example: Notification system.*
8. **State** - Allows an object to alter its behavior when its internal state changes.  
   *Example: Status of an order with different methods (New, Sent, Delivered).*
9. **Strategy** - Defines a family of algorithms, encapsulates each one, and makes them interchangeable.  
   *Example: Choosing a caching strategy (Memory or Disk).*
10. **Template Method** - Defines the skeleton of an algorithm, deferring some steps to subclasses.  
    *Example: Different payment methods (Stripe, PayPal) with different specifics but a common structure (validate/pay/log).*
11. **Visitor** - Allows new operations to be defined without changing the classes of the elements on which it operates.  
    *Example: Logging system.*
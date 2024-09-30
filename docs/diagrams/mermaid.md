Here are the three sequence diagrams broken down based on your requirements:

### 1) User Logging In and Creating a Ride

```mermaid
sequenceDiagram
    participant User
    participant System
    participant DB as Database
    
    %% Login Flow
    User->>System: Log in
    System->>DB: Validate credentials
    DB-->>System: Credentials valid
    System-->>User: Login successful
    
    %% Create Ride
    User->>System: Create Ride (with details)
    System->>DB: Store ride details
    DB-->>System: Ride created
    System-->>User: Ride added to My Rides
```

### 2) Different User Logging In, Searching for a Ride, and Joining

```mermaid
sequenceDiagram
    participant UserB as User
    participant System
    participant DB as Database
    
    %% Login Flow
    UserB->>System: Log in
    System->>DB: Validate credentials
    DB-->>System: Credentials valid
    System-->>UserB: Login successful
    
    %% Search Ride
    UserB->>System: Search Ride
    System->>DB: Fetch available rides
    DB-->>System: Rides list
    System-->>UserB: Display list of rides
    
    %% Join Ride
    UserB->>System: Join ride (selected)
    System->>DB: Add UserB to ride
    DB-->>System: Ride joined
    System-->>UserB: Show updated My Rides
```

### 3) User Opting Out / Deleting a Ride

```mermaid
sequenceDiagram
    participant User
    participant System
    participant DB as Database
    
    %% My Rides
    User->>System: View My Rides
    System->>DB: Fetch user rides
    DB-->>System: User rides list
    System-->>User: Display My Rides
    
    %% Opt out/Delete Ride
    User->>System: Opt out/Delete ride
    System->>DB: Update/Delete ride info
    DB-->>System: Ride info updated
    System-->>User: Update My Rides
```
# Install required libraries
!pip install pandas openpyxl

# Import necessary libraries
import pandas as pd

# Load the Instagram mock data
file_path = '/Instagram_MockData.xlsx'
data = pd.read_excel(file_path)

# Preview the first few rows of the data to understand its structure
data.head()

# Install necessary libraries for data manipulation and reading Excel files
!pip install pandas openpyxl



# Test User Authentication: Login success based on username and password
def test_user_authentication(data, username_input, password_input):
    # Check if username and password match any in the data
    user = data[(data['username'] == username_input) & (data['password'] == password_input)]

    if not user.empty:
        print(f"Login successful for user: {username_input}")
    else:
        print(f"Login failed for user: {username_input}")

# Example test
test_user_authentication(data, 'bansari11', 'password123')  # This should succeed
test_user_authentication(data, 'Jay', 'wrongPass')  # This should fail


# Test Posting and Interactions: Here we consider followers as interactions
def test_posting_and_interactions(data):
    data['num_followers'] = data['followers'].apply(lambda x: len(x.split(',')))  # Count number of followers
    print(data[['username', 'num_followers']])  # Display username and follower count

# Run the test
test_posting_and_interactions(data)


# Test Profile Management: User personas based on password type
def test_profile_management(data):
    # Categorize users based on their password type
    data['persona'] = data['password'].apply(
        lambda x: 'Content Creator/Influencer' if 'creator' in x else
                  'Business User' if 'business' in x else
                  'General User'
    )
    print(data[['username', 'persona']])

# Run the test
test_profile_management(data)


# Test Search Functionality: Searching users or followers
def test_search_functionality(data, search_query):
    # Check if the search_query is found in usernames or followers
    user_match = data[data['username'] == search_query]
    follower_match = data[data['followers'].str.contains(search_query)]

    if not user_match.empty:
        print(f"User found: {search_query}")
    elif not follower_match.empty:
        print(f"Follower found: {search_query}")
    else:
        print(f"No match found for: {search_query}")

# Example search tests
test_search_functionality(data, 'Parth')  # Should find Parth as both a user and a follower
test_search_functionality(data, 'Nayan')  # Should find Nayan as a follower
test_search_functionality(data, 'RandomUser')  # Should not find this user


import pandas as pd

# Sample DataFrame setup
data = pd.DataFrame({
    'username': ['Nayan', 'Jay', 'Ashish', 'Ravi', 'Butani'],
    'new_followers': [None] * 5  # Initialize with None
})

# Function to test notifications system
def test_notifications_system(data, new_followers):
    # Adding new followers to existing users
    data['new_followers'] = new_followers

    # Notify users who gained new followers
    for index, row in data.iterrows():
        if row['new_followers'] is not None:
            print(f"User {row['username']} received new followers: {row['new_followers']}")

# Simulating new followers for each user
new_followers_data = [3, 2, 5, None, 1]  # Numeric values for count of new followers
test_notifications_system(data, new_followers_data)


import pandas as pd

# Sample data creation
data = {
    'username': ['bansari11', 'butani', 'Ashish', 'Jay', 'Parth', 'Nayan'],
    'password': ['password123', 'password456', 'password789', 'creatorPass123', 'businessPass456', 'businessPass456'],
    'email': ['bansari11@.com', 'butani@.com', 'Ashish@.com', 'Jay.com', 'Parth@.com', 'Nayan@.com'],
    'followers': [
        ['Butani', 'Parth'],
        ['Nayan', 'Parth', 'Jay'],
        ['Butani', 'Parth'],
        ['Parth', 'Nayan'],
        ['Jay', 'Ashish'],
        ['bansari11', 'Butani']
    ],
    'persona': ['General User', 'Content Creator/Influencer', 'Content Creator/Influencer',
                'Content Creator/Influencer', 'Business User', 'Business User']
}

# Create a DataFrame
df = pd.DataFrame(data)

def identify_user_personas(data):
    # General User: Interacts with followers
    general_users = data[data['persona'] == 'General User']

    # Content Creator/Influencer: Special creator password
    content_creators = data[data['persona'] == 'Content Creator/Influencer']

    # Business User: Business password
    business_users = data[data['persona'] == 'Business User']

    print(f"General Users: {len(general_users)}")
    print(f"Content Creators/Influencers: {len(content_creators)}")
    print(f"Business Users: {len(business_users)}")

# Run the user persona identification
identify_user_personas(df)


# Mock function to simulate user login
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# Sample user database
users_db = {
    'bansari11': User('bansari11', 'password123', 'bansari11@.com'),
    'butani': User('butani', 'password456', 'butani@.com'),
    'Ashish': User('Ashish', 'password789', 'Ashish@.com'),
    'Jay': User('Jay', 'creatorPass123', 'Jay.com'),
    'Parth': User('Parth', 'businessPass456', 'Parth@.com'),
    'Nayan': User('Nayan', 'businessPass456', 'Nayan@.com')
}

def login(username, password):
    user = users_db.get(username)
    if user and user.password == password:
        return "Login successful"
    return "Login failed"

# Unit Tests for the login feature
def test_login():
    # Test valid credentials
    assert login('bansari11', 'password123') == "Login successful", "Test failed: valid credentials not working"
    assert login('butani', 'password456') == "Login successful", "Test failed: valid credentials not working"

    # Test invalid credentials
    assert login('bansari11', 'wrongpassword') == "Login failed", "Test failed: invalid password not caught"
    assert login('unknown_user', 'password123') == "Login failed", "Test failed: unknown user not caught"
    assert login('butani', 'wrongpassword') == "Login failed", "Test failed: invalid password not caught"

# Run the tests
test_login()
print("All login tests passed!")


class User:
    def __init__(self, username, password, email):
        # Initialize user with username, password, email, followers, and notifications
        self.username = username
        self.password = password
        self.email = email
        self.followers = []  # List of followers
        self.notifications = []  # List of notifications

    def follow(self, user):
        """Allow the user to follow another user."""
        user.followers.append(self)  # Add the user to the follower's list

    def post_content(self, content_type, content, caption):
        """User posts content and notifies followers."""
        post_info = {
            'username': self.username,
            'content_type': content_type,
            'content': content,
            'caption': caption
        }
        # Notify followers about the new post
        self.notify_followers(post_info)

    def notify_followers(self, post_info):
        """Send notifications to all followers about the new post."""
        for follower in self.followers:
            follower.receive_notification(f"{self.username} posted new {post_info['content_type']}: '{post_info['caption']}'")

    def receive_notification(self, message):
        """Receive a notification."""
        self.notifications.append(message)  # Append notification to the user's notifications list


# Example Setup
bansari = User('bansari11', 'password123', 'bansari11@.com')  # Create user Bansari
butani = User('butani', 'password456', 'butani@.com')  # Create user Butani
parth = User('Parth', 'businessPass456', 'Parth@.com')  # Create user Parth

# Establishing follower relationships
bansari.follow(butani)  # Bansari follows Butani
bansari.follow(parth)   # Bansari follows Parth

# Bansari posts content
bansari.post_content('photo', 'photo1.jpg', 'A beautiful sunset!')  # Bansari posts a photo

# Outputting notifications for followers
print("Notifications for followers of Bansari:")
for follower in bansari.followers:
    print(f"{follower.username}: {follower.notifications[-1]}")  # Display the last notification for each follower


# User class representing a user in the system
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.followers = []
        self.notifications = []
        self.posts = []

    def post_content(self, content_type, content, caption):
        post = {
            'username': self.username,
            'content_type': content_type,
            'content': content,
            'caption': caption,
            'likes': 0
        }
        self.posts.append(post)
        self.notify_followers(f"{self.username} posted new content")

    def notify_followers(self, message):
        for follower in self.followers:
            follower.receive_notification(message)

    def receive_notification(self, message):
        self.notifications.append(message)

    def like_post(self, post):
        post['likes'] += 1

    def comment_on_post(self, post, comment):
        post_id = len(post.get('comments', [])) + 1
        post.setdefault('comments', []).append({'post_id': post_id, 'username': self.username, 'comment': comment})

# Sample data for users
users = {
    'bansari11': User('bansari11', 'password123', 'bansari11@.com'),
    'butani': User('butani', 'password456', 'butani@.com'),
    'Ashish': User('Ashish', 'password789', 'Ashish@.com'),
    'Jay': User('Jay', 'creatorPass123', 'Jay.com'),
    'Parth': User('Parth', 'businessPass456', 'Parth@.com'),
    'Nayan': User('Nayan', 'businessPass456', 'Nayan@.com'),
}

# Establishing follower relationships (corrected the usernames to match the dictionary keys)
users['bansari11'].followers.extend([users['butani'], users['Parth']])  # Corrected 'Butani' to 'butani'
users['butani'].followers.extend([users['Nayan'], users['Parth'], users['Jay']])
users['Ashish'].followers.extend([users['butani'], users['Parth']])  # Corrected 'Butani' to 'butani'
users['Jay'].followers.extend([users['Parth'], users['Nayan']])
users['Parth'].followers.extend([users['Jay'], users['Ashish']])
users['Nayan'].followers.extend([users['bansari11'], users['butani']])  # Corrected 'Butani' to 'butani'

# User Login Simulation (for simplicity, we're not implementing a full login system)
def login(username, password):
    user = users.get(username)
    if user and user.password == password:
        return user
    return None

# Simulate User Flow
def test_complete_user_flow():
    # Step 1: Login
    user_bansari = login('bansari11', 'password123')
    assert user_bansari is not None, "Login failed for bansari11"

    # Step 2: Post Content
    user_bansari.post_content('photo', 'photo1.jpg', 'A beautiful sunset!')

    # Step 3: User likes their own post
    user_bansari.like_post(user_bansari.posts[0])

    # Step 4: User comments on their post
    user_bansari.comment_on_post(user_bansari.posts[0], "Wow, what a beautiful sunset!")

    # Step 5: Check Notifications for followers
    for follower in user_bansari.followers:
        assert f"{user_bansari.username} posted new content" in follower.notifications, f"Notification not received by {follower.username}"

# Execute the test
test_complete_user_flow()

print("All tests passed successfully!")


import re

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Test cases
emails = [
    "bansari11@.com",  # Invalid
    "butani@.com",     # Invalid
    "user@domain",     # Invalid
    "user@domain..com", # Invalid
    "bansari11@domain.com",  # Valid
    "butani@company.org"      # Valid
]

results = {email: is_valid_email(email) for email in emails}
print(results)


def is_valid_username(username):
    max_length = 15
    return 1 <= len(username) <= max_length

# Test cases
usernames = [
    "bansariusername",      # Valid (15 characters)
    "bansariusernametoo"    # Invalid (16 characters)
]

results = {username: is_valid_username(username) for username in usernames}
print(results)


def login(username, password):
    valid_credentials = {
        'bansari11': 'password123',
        'butani': 'password456'
    }
    return valid_credentials.get(username) == password

# Test cases
login_tests = [
    ('bansari11', 'password123'),  # Should succeed
    ('butani', 'password456'),      # Should succeed
    ('bansari11', 'wrongpass'),     # Should fail
    ('invalidUser', 'password123'), # Should fail
    ('bansari11', '')                # Should fail
]

results = {test: login(*test) for test in login_tests}
print(results)


def test_login_valid(username, password):
    valid_credentials = {'bansari11': 'password123'}
    assert valid_credentials.get(username) == password, "Login failed"

# Execute the test
test_login_valid('bansari11', 'password123')  # Should pass


def test_login_invalid(username, password):
    valid_credentials = {'bansari11': 'password123'}
    assert valid_credentials.get(username) != password, "Login should fail"

# Execute the test
test_login_invalid('bansari11', 'wrongpassword')  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.feed = []

    def upload_photo(self, photo):
        self.feed.append(photo)

# Test
user = User('bansari11')
user.upload_photo('photo1.jpg')
assert 'photo1.jpg' in user.feed  # Should pass


class Post:
    def __init__(self, post_id):
        self.post_id = post_id
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

# Test
post = Post(1)
post.add_comment("Wow, what a beautiful sunset!")
assert "Wow, what a beautiful sunset!" in post.comments  # Should pass



def search_profiles(query, profiles):
    return [profile for profile in profiles if query in profile]

# Test
profiles = ['bansari11', 'butani', 'Ashish']
assert search_profiles('bansari11', profiles) == ['bansari11']  # Should pass


def recover_password(email):
    valid_emails = ['bansari11@.com']
    return "Recovery email sent" if email in valid_emails else "Email not found"

# Test
assert recover_password('bansari11@.com') == "Recovery email sent"  # Should pass


class UserProfile:
    def __init__(self, email):
        self.email = email

    def update_email(self, new_email):
        self.email = new_email

# Test
user_profile = UserProfile('bansari11@.com')
user_profile.update_email('bansari11_new@.com')
assert user_profile.email == 'bansari11_new@.com'  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.notifications = []

    def add_notification(self, notification):
        self.notifications.append(notification)

# Test
user = User('butani')
user.add_notification('user1 liked your post')
assert 'user1 liked your post' in user.notifications  # Should pass


class UserProfile:
    def __init__(self):
        self.privacy_setting = 'Public'

    def update_privacy(self, setting):
        self.privacy_setting = setting

# Test
user_profile = UserProfile()
user_profile.update_privacy('Private')
assert user_profile.privacy_setting == 'Private'  # Should pass


class Post:
    def __init__(self, post_id):
        self.post_id = post_id
        self.likes = 0

    def like_post(self):
        self.likes += 1

# Test
post = Post(1)
post.like_post()
assert post.likes == 1  # Should pass


class Post:
    def __init__(self, post_id):
        self.post_id = post_id
        self.likes = 0

    def like_post(self):
        self.likes += 1

# Test
post = Post(1)
post.like_post()
assert post.likes == 1  # Should pass


class Post:
    def __init__(self, post_id):
        self.post_id = post_id
        self.reported = False

    def report_post(self):
        self.reported = True

# Test
post = Post(1)
post.report_post()
assert post.reported  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.logged_in = True

    def logout(self):
        self.logged_in = False

# Test
user = User('bansari11')
user.logout()
assert not user.logged_in  # Should pass


class UserProfile:
    def __init__(self, username):
        self.username = username
        self.details = f"{username}'s profile details"

    def view_profile(self):
        return self.details

# Test
user_profile = UserProfile('butani')
assert user_profile.view_profile() == "butani's profile details"  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.logged_in = True

    def logout(self):
        self.logged_in = False

# Test
user = User('bansari11')
user.logout()
assert not user.logged_in  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.feed = []

    def view_feed(self):
        return self.feed

# Test
user = User('bansari11')
user.feed = ['photo1.jpg', 'video1.mp4']
assert user.view_feed() == ['photo1.jpg', 'video1.mp4']  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.notifications = []

    def fetch_notifications(self):
        return self.notifications

# Test
user = User('bansari11')
user.notifications = ['New follower', 'Liked your photo']
assert user.fetch_notifications() == ['New follower', 'Liked your photo']  # Should pass


def test_login_valid(username, password):
    valid_credentials = {'bansari11': 'password123'}
    result = valid_credentials.get(username) == password
    print("Test Login with Valid Credentials: ", result)
    return result

# Execute the test
test_login_valid('bansari11', 'password123')  # Should pass


def test_login_invalid(username, password):
    valid_credentials = {'bansari11': 'password123'}
    result = valid_credentials.get(username) != password
    print("Test Login with Invalid Credentials: ", result)
    return result

# Execute the test
test_login_invalid('bansari11', 'wrongpassword')  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.feed = []

    def upload_photo(self, photo):
        self.feed.append(photo)

# Test
user = User('bansari11')
user.upload_photo('photo1.jpg')
result = 'photo1.jpg' in user.feed
print("Test Uploading a Photo: ", result)  # Should pass



class Post:
    def __init__(self, post_id):
        self.post_id = post_id
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

# Test
post = Post(1)
post.add_comment("Wow, what a beautiful sunset!")
result = "Wow, what a beautiful sunset!" in post.comments
print("Test Posting a Comment on a Post: ", result)  # Should pass


def search_profiles(query, profiles):
    return [profile for profile in profiles if query in profile]

# Test
profiles = ['bansari11', 'butani', 'Ashish']
result = search_profiles('bansari11', profiles)
print("Test Search Functionality: ", result)  # Should return ['bansari11']



def recover_password(email):
    valid_emails = ['bansari11@.com']
    return "Recovery email sent" if email in valid_emails else "Email not found"

# Test
result = recover_password('bansari11@.com')
print("Test Password Recovery: ", result)  # Should return "Recovery email sent"


class UserProfile:
    def __init__(self, email):
        self.email = email

    def update_email(self, new_email):
        self.email = new_email

# Test
user_profile = UserProfile('bansari11@.com')
user_profile.update_email('bansari11_new@.com')
result = user_profile.email == 'bansari11_new@.com'
print("Test Editing User Profile: ", result)  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.notifications = []

    def add_notification(self, notification):
        self.notifications.append(notification)

# Test
user = User('butani')
user.add_notification('user1 liked your post')
result = 'user1 liked your post' in user.notifications
print("Test Notifications: ", result)  # Should pass


class UserProfile:
    def __init__(self):
        self.privacy_setting = 'Public'

    def update_privacy(self, setting):
        self.privacy_setting = setting

# Test
user_profile = UserProfile()
user_profile.update_privacy('Private')
result = user_profile.privacy_setting == 'Private'
print("Test Privacy Settings: ", result)  # Should pass


class Post:
    def __init__(self, post_id):
        self.post_id = post_id
        self.likes = 0

    def like_post(self):
        self.likes += 1

# Test
post = Post(1)
post.like_post()
result = post.likes == 1
print("Test Like a Post: ", result)  # Should pass



class Post:
    def __init__(self, post_id):
        self.post_id = post_id
        self.reported = False

    def report_post(self):
        self.reported = True

# Test
post = Post(1)
post.report_post()
result = post.reported
print("Test Reporting a Post: ", result)  # Should pass


class User:
    def __init__(self, username):
        self.username = username
        self.logged_in = True

    def logout(self):
        self.logged_in = False

# Test
user = User('bansari11')
user.logout()
result = not user.logged_in
print("Test User Logout: ", result)  # Should pass


class UserProfile:
    def __init__(self, username):
        self.username = username
        self.details = f"{username}'s profile details"

    def view_profile(self):
        return self.details

# Test
user_profile = UserProfile('butani')
result = user_profile.view_profile()
print("Test Viewing User Profile: ", result)  # Should return "butani's profile details"

class User:
    def __init__(self, username):
        self.username = username
        self.feed = []

    def view_feed(self):
        return self.feed

# Test
user = User('bansari11')
user.feed = ['post1', 'post2']
result = user.view_feed()
print("Test Viewing Feed: ", result)  # Should return ['post1', 'post2']


class User:
    def __init__(self, username):
        self.username = username
        self.followers = []

    def follow(self, user_to_follow):
        self.followers.append(user_to_follow)

# Test
user = User('bansari11')
user.follow('Nayan')
result = 'Nayan' in user.followers
print("Test Following Another User: ", result)  # Should pass


# User data
valid_users = {
    'bansari11': 'password123',
    'butani': 'password456',
    'Ashish': 'password789',
    'Jay': 'creatorPass123',
    'Parth': 'businessPass456',
    'Nayan': 'businessPass456'
}

# Pseudo code for login test case
def test_user_login(username, password):
    # Simulate the login process
    if username in valid_users and valid_users[username] == password:
        return "Pass"  # Login successful
    else:
        return "Fail"  # Login failed

# Execute Test Case
result = test_user_login('bansari11', 'password123')
print(f'Test Case ID: TC001 | Steps: Login with username: bansari11, password: password123 | Expected: Pass | Actual: {result}')

# Additional test cases for demonstration
additional_tests = [
    ('butani', 'wrongpassword'),  # Should fail
    ('Ashish', 'password789'),     # Should pass
    ('nonexistent_user', 'anyPassword')  # Should fail
]

for username, password in additional_tests:
    result = test_user_login(username, password)
    print(f'Test Case | Steps: Login with username: {username}, password: {password} | Expected: {"Pass" if username in valid_users and valid_users[username] == password else "Fail"} | Actual: {result}')



# Pseudo code for content posting test case
def test_content_posting(username, content_type):
    # Simulate content posting
    if content_type in ['photo', 'video']:
        return "Pass"  # Content posted successfully
    else:
        return "Fail"  # Invalid content type

# Execute Test Case
result = test_content_posting('bansari11', 'photo')
print(f'Test Case ID: TC002 | Steps: Post a photo | Expected: Pass | Actual: {result}')





import pandas as pd

# Create a DataFrame to log defects
defect_data = {
    "Bug ID": [1, 2, 3],
    "Severity": ["Critical", "Major", "Minor"],
    "Description": [
        "User unable to log in with valid credentials",
        "Content not loading after posting",
        "Misspelled word in notification"
    ],
    "Steps to Reproduce": [
        "1. Go to login page.\n2. Enter valid username and password.\n3. Click login.",
        "1. Log in.\n2. Post new content.\n3. Refresh page.",
        "1. Log in.\n2. Check notifications.\n3. Observe the misspelled word."
    ],
    "Status": ["Open", "Assigned", "Resolved"]
}

# Create a DataFrame
defect_log = pd.DataFrame(defect_data)

# Save the defect log to an Excel file
defect_log.to_excel('defect_log.xlsx', index=False)

print("Defect log created successfully!")

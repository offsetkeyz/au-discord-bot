# au-discord-bot

au-discord-bot is a collaborative project aimed at helping students in the Auburn Online Computer Science discord server build projects collaboratively and add new skills to their resumes.

## Getting Started

To contribute to this project, follow these steps:

1.  Clone the repository to your local machine using the following command:

`git clone https://github.com/offsetkeyz/au-discord-bot.git` 

2.  Create a new branch using the following command:

`git checkout -b <new_branch_name>` 

3.  Make your changes to the code in your local repository.
    
4.  Test the changes in your own discord server to ensure that they work as expected.
    
5.  Commit the changes to your local repository using the following command:

`git commit -m "<commit_message>"` 

6.  Push the changes to your forked repository using the following command:

`git push origin <new_branch_name>` 

7.  Create a pull request on the main repository and describe the changes you made and why they are important.

## Testing

To test the bot, follow these steps:

1.  Create a new discord server for testing purposes.
    
2.  Obtain a bot token by creating a new bot application in the Discord Developer Portal.
    
3.  Create a `config.json` file in the root directory of the project with the following format:

`{
  "TOKEN": "your_bot_token_here"
}` 

Replace `your_bot_token_here` with your actual bot token.

4.  Install the necessary Python packages by running the following command:

`pip install -r requirements.txt` 

5.  Run the bot using the following command:

`python3 bot.py` 

6.  Invite your bot to your test server by using the OAuth2 URL generated in the Discord Developer Portal.
    
7.  Test the bot by typing commands with the prefix you specified in the `config.json` file in the text channels of your test server.
    

*Note: Make sure to keep your bot token and any other sensitive information secure and do not share them publicly.*

## Contributing

We welcome contributions from anyone who is interested in improving the functionality of this project. Please follow the steps outlined above to contribute.

If you're looking for ideas or inspiration, join the official Trello board by following this link: https://trello.com/invite/auburnonline/ATTIbd004a1dccfe684dde54c62b77fc8884825EEFA0

## License

This project is licensed under the [MIT License](https://chat.openai.com/LICENSE.md). By contributing to this project, you agree to the terms of this license.

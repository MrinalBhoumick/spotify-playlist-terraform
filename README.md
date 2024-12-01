# Creating Multiple Spotify Playlists Using Terraform

[GitHub Repo](https://github.com/MrinalBhoumick/spotify-playlist-terraform/tree/main)

## Project Overview

This project demonstrates how to use **Terraform** to automate the creation and management of multiple **Spotify playlists** for different occasions such as morning, evening, party nights, etc. Terraform will be used to configure and manage these playlists efficiently.

## Prerequisites

Before starting, ensure that you have the following:

1. **Terraform Installed**: Ensure Terraform is installed on your local machine.
2. **Docker Installed**: Make sure Docker is installed and running.
3. **Spotify Account**: A Spotify account is needed (Premium access is not required).
4. **Spotify Developer Account**: You must register and create an application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/), and obtain the `Client ID` and `Client Secret`.
5. **Spotify Provider for Terraform**: Install and configure the Spotify provider for Terraform.
6. **VS Code (Optional)**: Recommended for editing Terraform configuration files.

## Steps to Complete the Project

### 1. Create Terraform Project

Start by setting up your Terraform project:

1. Create a new directory for your Terraform project and navigate to it.
2. Create a file named `provider.tf` in this directory.

### 2. Define Spotify Provider

In the `provider.tf` file, define the Spotify provider by adding the following code:

```hcl
provider "spotify" {
  api_key = "YOUR_SPOTIFY_API_KEY"
}
```

### 3. Obtain API Key

To interact with Spotify's API, you will need a `Client ID` and `Client Secret` from your Spotify Developer account.

### 4. Create a Spotify App

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on "Create an App."
4. Fill in the necessary details and create the app.

    **Example details:**
    - **App Name**: My Playlist through Terraform
    - **Description**: Automate the creation of multiple Spotify playlists using Terraform.
    - **Redirect URIs**: `http://localhost:27228/spotify_callback`

5. After creating the app, note down the `Client ID` and `Client Secret`.

### 5. Store Credentials

Create a `.env` file in your project directory to store your Spotify application's credentials:

```
SPOTIFY_CLIENT_ID=<your_spotify_client_id>
SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>
```

### 6. Run the Spotify Auth App to Get API Key

Ensure that **Docker** is running and start the authorization proxy server:

```bash
docker run --rm -it -p 27228:27228 --env-file .env ghcr.io/conradludgate/spotify-auth-proxy
```

This will authenticate and get the API key for interacting with Spotify. You should see an "Authorization Successful" message.

### 7. Complete Terraform Code

Continue to build the rest of the Terraform configuration for creating the playlists and adding tracks.

### 8. Terraform Commands to Initialize, Validate, and Apply Configuration

Once your Terraform code is ready, run the following commands to initialize, validate, and apply the configuration.

#### Initialize Terraform

Initialize your Terraform configuration by running:

```bash
terraform init
```

This command downloads the necessary provider plugins and sets up your working directory for Terraform operations.

#### Validate Configuration

Validate your Terraform configuration to ensure that there are no syntax errors:

```bash
terraform validate
```

#### Plan the Execution

Generate an execution plan to review what changes Terraform will make:

```bash
terraform plan
```

This step is important as it shows you the resources Terraform will create, modify, or destroy.

#### Apply Configuration

Finally, apply the configuration to create the Spotify playlists. Use the `-auto-approve` flag to automatically approve the changes:

```bash
terraform apply -auto-approve
```

This command will create the playlists and manage the resources defined in your configuration.

### 9. Verify Playlists

After applying the Terraform configuration, log in to your Spotify account and verify that the playlists have been created and populated with the specified tracks.

## Conclusion

By following the steps outlined in this guide, you will automate the creation and management of multiple Spotify playlists using Terraform. This method saves time and ensures that playlists are consistently created with the tracks you want. You can customize the playlists for different occasions and use the same approach to add or modify playlists in the future.

---
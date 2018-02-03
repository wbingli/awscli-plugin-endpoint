awscli-plugin-endpoint
=============

This awscli plugin provides service endpoint configure **per service** on profile.

------------
Installation
------------

The easiest way to install awscli-plugin-endpoint is to use `pip`:

    $ pip install awscli-plugin-endpoint

or, if you install `awscli` via Homebrew, which bundles its own python, install as following:

    $ /usr/local/opt/awscli/libexec/bin/pip install awscli-plugin-endpoint


---------------
Getting Started
---------------

Before using awscli-plugin-endpoint plugin, you need to [configure awscli](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) first.

**MUST**: Once that's done, to enable `awscli-plugin-endpoint` plugin, you can run:

    $ aws configure set plugins.endpoint awscli_plugin_endpoint

The above command adds below section to your aws config file. You can also directly edit your `~/.aws/config` with below configuration.

    [plugins]
    endpoint = awscli_plugin_endpoint

To add endpoint configure to a profile(assuming you have a **local** profile), you can run:

    $ aws configure --profile local set dynamodb.endpoint_url http://localhost:8000

The above command adds below section to your profile:

    [profile local]
    dynamodb =
        endpoint_url = http://localhost:8000

Now you can access your local dynamodb just use profile:

    $ aws dynamodb list-tables --profile local

## One more example with S3 configuration

Add endpoint configuration to the profile:

    $ aws configure --profile wasabi set s3.endpoint_url https://s3.wasabisys.com

The profile will looks like below:

    [profile wasabi]
    region = us-east-1
    s3 =
        endpoint_url = https://s3.wasabisys.com

Now you can use `aws s3` command with this profile as following:

    $ aws s3 ls --profile wasabi

One more thing, the endpoint is technically per **sub command**. Take S3 as example, above S3 configuration will not work for S3 low level CLI `aws s3api`.  To make `s3api` work with this endpoint, you should add endpoint to this sub command as well:

    [profile wasabi]
    region = us-east-1
    s3 =
        endpoint_url = https://s3.wasabisys.com
    s3api =
        endpoint_url = https://s3.wasabisys.com

Now you can use `aws s3api` command with this profile as following:

    $ aws s3api --profile wasabi list-buckets


`verify_ssl` Support
------------------
To allow insecure/self-signed ssl certificates:

    [profile local]
    dynamodb =
        verify_ssl = false
        endpoint_url = https://localhost:8000

To disable Unverified HTTPS request warning, export:

    export PYTHONWARNINGS="ignore:Unverified HTTPS request"

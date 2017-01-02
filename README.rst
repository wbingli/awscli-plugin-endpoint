=============
awscli-plugin-endpoint
=============

This awscli plugin provides service endpoint configure on profile.

------------
Installation
------------

The easiest way to install awscli-plugin-endpoint is to use `pip`::

    $ pip install awscli-plugin-endpoint

or, if you are not installing in a ``virtualenv``::

    $ sudo pip install awscli-plugin-endpoint

or, if you install `awscli` via Homebrew, which bundles its own python, install as following::

    $ /usr/local/opt/awscli/libexec/bin/pip install awscli-plugin-endpoint

If you have the awscli-plugin-endpoint installed and want to upgrade to the latest version
you can run::

    $ pip install --upgrade awscli-plugin-endpoint

This will install the awscli-plugin-endpoint package as well as all dependencies, including awscli.

---------------
Getting Started
---------------

Before using awscli-plugin-endpoint plugin, you need to `configure awscli <http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html>`__ first.

Once that's done, to enable awscli-plugin-endpoint, you can run::

    $ aws configure set plugins.endpoint awscli_plugin_endpoint

The above command adds below section to your aws config file::

    [plugins]
    endpoint = awscli_plugin_endpoint

To add endpoint configure to a profile(assuming you have a **local** profile), you can run::

    $ aws configure --profile local set dynamodb.endpoint_url http://localhost:8000

The above command adds below section to your profile::

    [profile local]
    dynamodb =
        endpoint_url = http://localhost:8000

Now you can access your local dynamodb just use profile::

    $ aws dynamodb list-tables --profile local



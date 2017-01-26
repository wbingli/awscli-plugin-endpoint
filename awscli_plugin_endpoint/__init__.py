ENDPOINT_URL = 'endpoint_url'
VERIFY_SSL = 'verify_ssl'

def str2bool(value):
    return str(value).lower() in ['1', 'yes', 'y', 'true', 'on']

def get_verify_from_profile(profile, command):
    verify = True
    if command in profile:
        if VERIFY_SSL in profile[command]:
            verify = str2bool(profile[command][VERIFY_SSL])
    return verify

def get_endpoint_from_profile(profile, command):
    endpoint = None
    if command in profile:
        if ENDPOINT_URL in profile[command]:
            endpoint = profile[command][ENDPOINT_URL]
    return endpoint

def set_endpoint_from_profile(parsed_args, **kwargs):
    endpoint_url = parsed_args.endpoint_url
    command = parsed_args.command
    # If endpoint set on CLI option, use CLI endpoint
    if endpoint_url is None:
        session = kwargs['session']
        # Set profile to session so we can load profile from config
        if parsed_args.profile:
            session.set_config_variable('profile', parsed_args.profile)
        service_endpoint = get_endpoint_from_profile(session.get_scoped_config(), command)
        if service_endpoint is not None:
            parsed_args.endpoint_url = service_endpoint

def set_verify_from_profile(parsed_args, **kwargs):
    verify_ssl = parsed_args.verify_ssl
    command = parsed_args.command
    # By default verify_ssl is set to true
    # if --no-verify-ssl is specified, parsed_args.verify_ssl is False
    # so keep it
    if verify_ssl:
        session = kwargs['session']
        # Set profile to session so we can load profile from config
        if parsed_args.profile:
            session.set_config_variable('profile', parsed_args.profile)
        service_verify = get_verify_from_profile(session.get_scoped_config(), command)
        if service_verify is not None:
            parsed_args.verify_ssl = service_verify

def awscli_initialize(cli):
    cli.register('top-level-args-parsed', set_endpoint_from_profile)
    cli.register('top-level-args-parsed', set_verify_from_profile)

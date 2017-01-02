ENDPOINT_URL = 'endpoint_url'

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

def awscli_initialize(cli):
    cli.register('top-level-args-parsed', set_endpoint_from_profile)

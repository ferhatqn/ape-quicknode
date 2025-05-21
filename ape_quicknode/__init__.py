from ape import plugins


@plugins.register(plugins.ProviderPlugin)
def providers():
    from .constants import QUICKNODE_NETWORKS
    from .provider import QuickNode

    for ecosystem_name in QUICKNODE_NETWORKS:
        for network_name in QUICKNODE_NETWORKS[ecosystem_name]:
            yield ecosystem_name, network_name, QuickNode


def __getattr__(name: str):
    if name == "NETWORKS":
        from .constants import QUICKNODE_NETWORKS

        return QUICKNODE_NETWORKS

    if name == "QuickNode":
        from .provider import QuickNode

        return QuickNode

    raise AttributeError(name)

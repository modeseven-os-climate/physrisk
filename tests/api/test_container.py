import fsspec.implementations.local as local
from dependency_injector import containers, providers

from physrisk.data.inventory_reader import InventoryReader

from ..data.test_hazard_model_store import mock_hazard_model_store_heat


class TestContainer(containers.DeclarativeContainer):
    __test__ = False

    config = providers.Configuration(default={"zarr_sources": ["embedded"]})

    inventory_reader = providers.Singleton(
        lambda: InventoryReader(fs=local.LocalFileSystem(), base_path="")
    )

    zarr_store = providers.Singleton(lambda: mock_hazard_model_store_heat([0], [0]))

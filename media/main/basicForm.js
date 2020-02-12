class Form {
    constructor(modelId, modelNamePlural, modelNameSingular, csrf_token, pType) {
        this.modelId = modelId;
        this.csrf_token = csrf_token;
        this.modelNamePlural = modelNamePlural;
        this.modelNameSingular = modelNameSingular;

        if (!pType || pType === "index") {
            this.createDeleteModal();
        }
    }

    createDeleteModal() {
        let textConfirm = $("<p>").html(`¿Está seguro que quiere eliminar el registro de ${this.modelNameSingular}?`);
        let btnClose = $("<button>").addClass("btn btn-default").attr({"type":"button", "data-dismiss":"modal"}).html("Cancelar");
        let btnSave = $("<button>").addClass("btn btn-primary").attr({"type":"button"}).html("Cancelar").on('click',function(){
            this.delete();
        });

        let modalBody = $("<div>").addClass("modal-body").append(textConfirm);
        let modalFooter = $("<div>").addClass("modal-footer").append([btnClose, btnSave]);
        let modalTitle = $("<div>").addClass("modal-title");
        let spanCloseText = $("<span>").attr({"aria-hidden":"true"}).html("&times;");
        let modalBtnTClose = $("<button>").attr({"type":"button", "data-dismiss":"modal", "aria-label":"Cerrar"}).addClass("close").append(spanCloseText);
        let modalHeader = $("<div>").addClass("modal-header").append([modalTitle, modalBtnTClose]);
        let modalContent = $("<div>").addClass("modal-content").append([modalHeader, modalBody, modalFooter]);
        let modalDialog = $("<div>").addClass("modal-dialog modal-sm").append(modalContent);
        let divModal = $("<div>").addClass("modal fade").attr("id", "deleteModal").append(modalDialog);
        $("body").append(divModal);
    }

    confirmDelete() {
        $("#deleteModal").modal("show");
    }

    delete() {

    }


}
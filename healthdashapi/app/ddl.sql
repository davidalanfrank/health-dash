"CREATE TABLE public.core_document (
	document_id INT8 NOT NULL DEFAULT unique_rowid(),
	user_id INT8 NOT NULL,
	document_type VARCHAR(255) NOT NULL,
	location VARCHAR(255) NULL,
	doc_label_exception_id BOOL NULL,
	name VARCHAR(255) NOT NULL,
	file_type VARCHAR(50) NOT NULL,
	status VARCHAR(50) NOT NULL,
	created_at TIMESTAMPTZ NULL DEFAULT now():::TIMESTAMPTZ,
	updated_at TIMESTAMPTZ NULL DEFAULT now():::TIMESTAMPTZ,
	CONSTRAINT core_document_pkey PRIMARY KEY (document_id ASC)
);"
"CREATE TABLE public.document_label_exception (
	exception_id INT8 NOT NULL DEFAULT unique_rowid(),
	s3_loc VARCHAR(255) NOT NULL,
	created_at TIMESTAMPTZ NULL DEFAULT now():::TIMESTAMPTZ,
	updated_at TIMESTAMPTZ NULL DEFAULT now():::TIMESTAMPTZ,
	CONSTRAINT document_label_exception_pkey PRIMARY KEY (exception_id ASC)
);"
"CREATE TABLE public.document_categories (
	category_id INT8 NOT NULL DEFAULT unique_rowid(),
	category_name VARCHAR(50) NOT NULL,
	created_at TIMESTAMPTZ NULL DEFAULT now():::TIMESTAMPTZ,
	updated_at TIMESTAMPTZ NULL DEFAULT now():::TIMESTAMPTZ,
	CONSTRAINT document_categories_pkey PRIMARY KEY (category_id ASC),
	UNIQUE INDEX document_categories_category_name_key (category_name ASC)
);"
"CREATE TABLE public.dexa_t_score (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	l_arm FLOAT4 NULL,
	r_arm FLOAT4 NULL,
	l_ribs FLOAT4 NULL,
	r_ribs FLOAT4 NULL,
	t_spine FLOAT4 NULL,
	l_spine FLOAT4 NULL,
	pelvis FLOAT4 NULL,
	l_leg FLOAT4 NULL,
	r_leg FLOAT4 NULL,
	subtotal FLOAT4 NULL,
	head FLOAT4 NULL,
	total FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_t_score_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_z_score (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	l_arm FLOAT4 NULL,
	r_arm FLOAT4 NULL,
	l_ribs FLOAT4 NULL,
	r_ribs FLOAT4 NULL,
	t_spine FLOAT4 NULL,
	l_spine FLOAT4 NULL,
	pelvis FLOAT4 NULL,
	l_leg FLOAT4 NULL,
	r_leg FLOAT4 NULL,
	subtotal FLOAT4 NULL,
	head FLOAT4 NULL,
	total FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_z_score_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_bmi (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	classification VARCHAR(255) NULL,
	bmi FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_bmi_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_est_vis_adi_tissue (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	est_vat VARCHAR(55) NULL,
	mass_g INT8 NULL,
	volume_cm3 INT8 NULL,
	area_cm2 FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_est_vis_adi_tissue_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_fat (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	percentile_am FLOAT4 NULL,
	percentile_yn FLOAT4 NULL,
	l_arm FLOAT4 NULL,
	r_arm FLOAT4 NULL,
	trunk FLOAT4 NULL,
	l_leg FLOAT4 NULL,
	r_leg FLOAT4 NULL,
	subtotal FLOAT4 NULL,
	head FLOAT4 NULL,
	total FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_fat_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_fat_mass_height_squared (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	kg_per_m2 FLOAT4 NULL,
	android_gynoid_ratio FLOAT4 NULL,
	fat_percent_trunk_legs FLOAT4 NULL,
	trunk_limb_fat_mass_ratio FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_fat_mass_height_squared_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_lean_mass (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	l_arm FLOAT4 NULL,
	r_arm FLOAT4 NULL,
	trunk FLOAT4 NULL,
	l_leg FLOAT4 NULL,
	r_leg FLOAT4 NULL,
	subtotal FLOAT4 NULL,
	head FLOAT4 NULL,
	total FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_lean_mass_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_lean_plus_bmc (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	l_arm FLOAT4 NULL,
	r_arm FLOAT4 NULL,
	trunk FLOAT4 NULL,
	l_leg FLOAT4 NULL,
	r_leg FLOAT4 NULL,
	subtotal FLOAT4 NULL,
	head FLOAT4 NULL,
	total FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_lean_plus_bmc_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa_total_mass (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	l_arm FLOAT4 NULL,
	r_arm FLOAT4 NULL,
	trunk FLOAT4 NULL,
	l_leg FLOAT4 NULL,
	r_leg FLOAT4 NULL,
	subtotal FLOAT4 NULL,
	head FLOAT4 NULL,
	total FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_total_mass_pkey PRIMARY KEY (id ASC)
);"
"CREATE TABLE public.dexa (
	dexa_id INT8 NOT NULL DEFAULT unique_rowid(),
	t_score_id INT8 NULL,
	z_score_id INT8 NULL,
	bmi_id INT8 NULL,
	fat_id INT8 NULL,
	fat_mass_height_squared DECIMAL(10,2) NULL,
	almi_id INT8 NULL,
	lean_mass_id INT8 NULL,
	lean_plus_bmc_id INT8 NULL,
	total_mass_id INT8 NULL,
	raw_location VARCHAR(255) NOT NULL,
	est_vat_id INT8 NULL,
	CONSTRAINT dexa_pkey PRIMARY KEY (dexa_id ASC)
);"
"CREATE TABLE public.dexa_almi (
	id INT8 NOT NULL DEFAULT unique_rowid(),
	kg_per_m2_yn FLOAT4 NULL,
	kg_per_m2_am FLOAT4 NULL,
	created_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	updated_at TIMESTAMP NULL DEFAULT current_timestamp():::TIMESTAMP,
	CONSTRAINT dexa_almi_pkey PRIMARY KEY (id ASC)
);"

